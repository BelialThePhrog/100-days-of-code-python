import requests
from bs4 import BeautifulSoup
import webbrowser
import random

TAXONOMY = {
    "Computer Science": {
        "Artificial Intelligence": "cs.AI",
        "Machine Learning": "cs.LG",
        "Computation and Language (NLP)": "cs.CL",
        "Computer Vision": "cs.CV",
    },
    "Physics": {
        "Astrophysics": "astro-ph",
        "Quantum Physics": "quant-ph",
    },
    "Mathematics": {
        "Combinatorics": "math.CO",
        "Statistics Theory": "math.ST",
    },
}

def choose_from(options, prompt="Choose one: "):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Please enter a valid number.")

def fetch_articles(category_code, max_results=15):
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=cat:{category_code}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={max_results}"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="xml")
    entries = soup.find_all("entry")
    return entries

def parse_entry(entry):
    title = entry.find("title").get_text(strip=True)
    pdf_tag = entry.find("link", title="pdf")
    pdf_url = pdf_tag["href"] if pdf_tag else None
    return {"title": title, "pdf_url": pdf_url}

def open_in_chrome(url):
    webbrowser.open(url)

def main():
    area_names = list(TAXONOMY.keys())
    area_index = choose_from(area_names, "Choose your area of interest: ")
    chosen_area = area_names[area_index]

    subareas = TAXONOMY[chosen_area]
    subarea_names = list(subareas.keys())
    subarea_index = choose_from(subarea_names, "Choose your sub-area: ")
    chosen_subarea = subarea_names[subarea_index]
    category_code = subareas[chosen_subarea]

    print(f"\nFetching recent articles in {chosen_subarea}...\n")
    raw_entries = fetch_articles(category_code)
    articles = [parse_entry(e) for e in raw_entries]

    if not articles:
        print("No articles found. Try a different sub-area.")
        return

    titles = [a["title"] for a in articles]
    menu_options = titles + ["Open random"]
    pick_index = choose_from(menu_options, "Choose an article: ")

    if pick_index == len(titles):
        chosen_article = random.choice(articles)
    else:
        chosen_article = articles[pick_index]

    print(f"\nOpening: {chosen_article['title']}")
    if chosen_article["pdf_url"]:
        open_in_chrome(chosen_article["pdf_url"])
    else:
        print("Sorry, no PDF link found for this article.")

if __name__ == "__main__":
    main()
