import requests
from bs4 import BeautifulSoup
import json
import time

def get_game_info(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        if response.status_code != 200:
            print(f"Failed to fetch: {url}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # Title
        title_tag = soup.find("div", class_="apphub_AppName")
        title = title_tag.text.strip() if title_tag else "Unknown"

        # Release Date
        release_date_tag = soup.find("div", class_="date")
        release_date = release_date_tag.text.strip() if release_date_tag else "Unknown"

        # Rating (e.g. "Very Positive")
        rating_tag = soup.find("span", class_="game_review_summary")
        rating = rating_tag.text.strip() if rating_tag else "No Rating"

        # Pricing
        discount_price_tag = soup.find("div", class_="discount_final_price")
        original_price_tag = soup.find("div", class_="discount_original_price")

        # Normal price (not discounted)
        regular_price_tag = soup.find("div", class_="game_purchase_price")

        if discount_price_tag and original_price_tag:
            on_sale = True
            sale_price = discount_price_tag.text.strip()
            original_price = original_price_tag.text.strip()
        elif regular_price_tag:
            on_sale = False
            sale_price = None
            original_price = regular_price_tag.text.strip()
        else:
            on_sale = False
            sale_price = None
            original_price = "Free" if "Free to Play" in response.text else "Unknown"

        return {
            "url": url,
            "title": title,
            "release_date": release_date,
            "rating": rating,
            "on_sale": on_sale,
            "original_price": original_price,
            "sale_price": sale_price
        }

    except Exception as e:
        print(f"Error with {url}: {e}")
        return None
# Load your saved sitemap file
with open("steamsitemap.xml", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "xml")

# Extract all <loc> entries (which may be game pages or more sitemaps)
urls = [loc.text for loc in soup.find_all("loc")]

# Keep only actual game links
game_urls = [url for url in urls if "/app/" in url]

# Save them into urls.json for your game scraper
with open("urls.json", "w") as f:
    json.dump(game_urls, f, indent=2)

print(f"Saved {len(game_urls)} game URLs to urls.json")

#new edition 
def main():
    # Load URLs from your existing urls.json file
    try:
        with open("urls.json", "r", encoding="utf-8") as f:
            game_urls = json.load(f)
    except FileNotFoundError:
        print("urls.json not found.")
        return

    games_data = []
    for index, url in enumerate(game_urls):
        print(f"Scraping {index + 1}/{len(game_urls)}: {url}")
        info = get_game_info(url)
        if info:
            games_data.append(info)
        time.sleep(1)  # Be polite

    # Save full data to games.json
    with open("games.json", "w", encoding="utf-8") as f:
        json.dump(games_data, f, indent=2, ensure_ascii=False)

    print(f"Saved game data for {len(games_data)} games to games.json")

if __name__ == "__main__":
    main()