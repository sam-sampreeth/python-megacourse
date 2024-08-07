try:
    width = float(input("Enter the width of rectangle:"))
    length = float(input("Enter the length of rectangle:"))
    if width == length:
        exit("That is a square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")
