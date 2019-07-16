# Scrasping news headlines using Python3 with BeautifulSoup
import requests
from bs4 import BeautifulSoup
import json


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)


url = 'https://inshorts.com/en/read'
response = requests.get(url)
print_headlines(response.text)