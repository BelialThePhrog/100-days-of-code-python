from bs4 import BeautifulSoup
import requests
from __future__ import print_function

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
text_to_work = response.text

# print(text_to_work)

soup = BeautifulSoup(text_to_work, "html.parser")
articles = soup.find_all(name="h3", class_="title")

article_text = []

for article_tag in articles[::-1]:
    text = article_tag.getText()
    if text != "Buy the film here":
        article_text.append(text)

with open("Movies_to_watch.txt", "a", encoding="utf-8") as f:
    for movie in article_text:
        f.write(f"{movie}\n")
