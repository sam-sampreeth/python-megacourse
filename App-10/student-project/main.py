from datetime import datetime
import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape page from url"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(src):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(src)["temperatures"]
    return value

def store(extracted):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open("data1.txt", "a") as file:
        line = f"{now}, {extracted}\n"
        file.write(line)

def read(extracted):
    with open("data1.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)