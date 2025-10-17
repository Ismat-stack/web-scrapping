import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://www.tpointtech.com/"

def get_soup(url):
    """Fetch webpage and return BeautifulSoup object"""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def scrape_tpointtech():
    """Scrape tutorial links and contact info from tpointtech.com"""
    soup = get_soup(BASE_URL)
    data = {}

    # ---------- Step 1: Extract Tutorials ----------
    tutorials = []
    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]
        if "tutorial" in href.lower():
            tutorials.append({
                "Tutorial Name": title,
                "Tutorial URL": urljoin(BASE_URL, href)
            })
    # Remove duplicates
    tutorials = list({t["Tutorial URL"]: t for t in tutorials}.values())
    data["Tutorials"] = tutorials

    # ---------- Step 2: Extract Contact Info ----------
    contact_info = {}

    # Get all visible text
    text = soup.get_text(separator="\n", strip=True)
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # 1️⃣ Extract email
    email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    emails = email_pattern.findall(text)
    if emails:
        contact_info["Email"] = emails[0]

    # 2️⃣ Extract phone number
    phone_pattern = re.compile(r"(\+91[-\s]?\d{10,})")
    phones = phone_pattern.findall(text)
    if phones:
        contact_info["Phone"] = phones[0]

    # 3️⃣ Extract address (look for keywords)
    address_line = next((line for line in lines if "Noida" in line or "India" in line or "Sec-3" in line), None)
    if address_line:
        contact_info["Address"] = address_line

    # 4️⃣ If we found nothing, tell user
    if not contact_info:
        contact_info["Error"] = "Contact info not found. Structure may have changed."

    data["Contact Info"] = contact_info
    return data


# ---------- Step 3: Display Results Nicely ----------
if __name__ == "__main__":
    result = scrape_tpointtech()

    print("\n🧑‍💻  TPOINTTECH.COM - SCRAPED DATA")
    print("=" * 60)

    # Tutorials
    print("\n📘 Available Tutorials:")
    for i, t in enumerate(result["Tutorials"], 1):
        print(f"{i}. {t['Tutorial Name']}")
        print(f"   🔗 {t['Tutorial URL']}")

    # Contact Info
    print("\n📞 Contact Information:")
    for key, value in result["Contact Info"].items():
        print(f"{key}: {value}")
