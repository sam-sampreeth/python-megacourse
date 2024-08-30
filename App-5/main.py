import requests
api_key = "ff370c0d89aa43f881c8b3405f454cd7"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-08-29&to=2024-08-29&sortBy=popularity&apiKey=ff370c0d89aa43f881c8b3405f454cd7"
reqs = requests.get(url)
cont = reqs.json()
for article in cont["articles"]:
    print(article["title"])