import streamlit
import requests

apikey = 'mioVpta6NMfD4zMAFO06mGkdJPWfPOvLmiK8Mc3t'
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

res1= requests.get(url)
data = res1.json()

titlee = data['title']
img_url = data['hdurl']
desc = data['explanation']

imgPath = "img.jpg"
res2 = requests.get(img_url)
with open(imgPath, 'wb') as f:
    f.write(res2.content)

streamlit.title(titlee)
streamlit.image(imgPath)
streamlit.write(desc)