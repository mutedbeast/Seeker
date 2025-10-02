import requests
from seeker import domain

def get_index_from_sitemap(domain):
    sitemap = requests.get(f"{domain}/sitemap.xml")
    site_map_text = sitemap.text
    return site_map_text

