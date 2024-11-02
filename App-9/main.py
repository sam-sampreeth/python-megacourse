import glob
import cv2
import time
from mailer import send_email

video = cv2.VideoCapture(0)
time.sleep(1)

frame1 = None
status_list = []
count = 1

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (15, 15), 0)

    if frame1 is None:
        frame1 = gray_frame_gau

    delta_frame = cv2.absdiff(frame1, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow('Video', dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_img = glob.glob(f"images/*.png")
            index = int(len(all_img) / 2)
            image_with_obj = all_img[index]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    print(status_list)

    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()