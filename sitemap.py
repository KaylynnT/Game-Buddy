import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
def get_links(url, domain):
    """Extracts all valid internal links from the given URL."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return set()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)
            
            if parsed_url.netloc == domain:  # Ensure it's an internal link
                links.add(full_url)
        
        return links
    except requests.RequestException:
        return set()

def crawl_website(start_url):
    """Crawls the website starting from start_url and collects all internal links."""
    domain = urlparse(start_url).netloc
    urls_to_visit = {start_url}
    visited_urls = set()
    
    while urls_to_visit:
        url = urls_to_visit.pop()
        if url not in visited_urls:
            visited_urls.add(url)
            urls_to_visit.update(get_links(url, domain))
    
    return visited_urls

def generate_sitemap(urls, output_file="sitemap.xml"):
    """Generates an XML sitemap from a list of URLs."""
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for url in sorted(urls):
        url_element = ET.SubElement(urlset, "url")
        loc_element = ET.SubElement(url_element, "loc")
        loc_element.text = url
    
    tree = ET.ElementTree(urlset)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Sitemap generated: {output_file}")

if __name__ == "__main__":
    website_url = "https://store.steampowered.com/"
    urls = crawl_website(website_url)
    generate_sitemap(urls)