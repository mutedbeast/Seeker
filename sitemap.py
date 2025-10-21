#Sitemap will be implemented in future updates

import requests
import xml.etree.ElementTree as xml


def get_sitemap(domain):
    sitemap = requests.get(f"{domain}/sitemap.xml")
    site_map_text = sitemap.text
    sitemap_xml = xml(site_map_text)
    root = xml.fromstring(sitemap_xml)
    loc_texts = [loc.text for loc in root.findall('.//loc')]
    print(loc_texts)

get_sitemap('https://www.chatgpt.com')