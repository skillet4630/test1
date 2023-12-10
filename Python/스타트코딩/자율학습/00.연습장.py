import requests
from bs4 import BeautifulSoup

def crawl_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('a', {'title': lambda x: x and 'Public' in x})

def main():
    base_url = "https://rargb.to/"
    search_query = "publicagent 1080p x265"
    search_url = f"{base_url}search/1/?search={search_query}"

    search_results = crawl_page(search_url)

    if not search_results:
        print("No results found.")
        return

    for link in search_results:
        print(f"Title: {link['title']}")

if __name__ == "__main__":
    main()
