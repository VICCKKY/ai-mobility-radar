import requests
from bs4 import BeautifulSoup
URL = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    page = requests.get(URL, headers=headers, timeout=10)
    page.raise_for_status()
except requests.RequestException as error:
    print(f"Website-ஐ திறக்க முடியவில்லை: {error}")
    raise SystemExit(1)

soup = BeautifulSoup(page.text, "html.parser")
items = soup.select(".titleline > a")
headlines = []
seen = set()

for item in items:
    title = " ".join(item.get_text(" ", strip=True).split())

    if not title or title.casefold() in seen:
        continue

    seen.add(title.casefold())
    headlines.append(title)

    if len(headlines) == 5:
        break

for number, title in enumerate(headlines, start=1):
    print(f"{number}. {title}")

if len(headlines) < 5:
    print(f"Only {len(headlines)} headlines found.")