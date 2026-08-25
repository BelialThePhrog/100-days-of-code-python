```python
from bs4 import BeautifulSoup

with open("website.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.a)

tags = soup.find_all(name="a")
for tag in tags:
    print(tag.getText())

for tag in tags:
    print(tag.get("href"))

headings = soup.find_all(name="h1", id="name")
print(headings)

company_url = soup.select_one(selector="p a")
print(company_url)
company_url = soup.select_one(selector="#name")
print(company_url)
