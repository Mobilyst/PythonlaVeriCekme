import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred= credentials.Certificate("Kampanyalar\mobilyst-135d1-firebase-adminsdk-ok765-4049e4f57f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

r = requests.get("https://www.sbarro.com.tr/kampanyalar-ve-promosyonlar#paket-servis-kampanyalari", verify=False)
soup = BeautifulSoup(r.content, "html.parser")
baslik = soup.find_all("span", attrs={"class": "title"})
resim = soup.find_all("span", attrs={"class": "picture"})
sayfa = soup.find_all("article", attrs={"class": "campaign"})

for idx, (a, b, c) in enumerate(zip(baslik, resim, sayfa)):
    title = a.text.strip()
    img = b.find("img")
    if img is not None:
        img_url = img["src"]
        img_url_relative = img["src"]
        img_url_absolute = urljoin(r.url, img_url_relative)
    sayfa_url = c.find("a")
    if sayfa_url is not None:
        url_relative  = sayfa_url["href"]
        url_absolute = urljoin(r.url, url_relative)

    
    campaign_id = f"sbarro_campaign_{idx}"

    
    data = {
        "Baslik": title,
        "ResimUrl": img_url_absolute,
        "SayfaUrl": url_absolute
    }
    db.collection("kampanyalar").document(campaign_id).set(data)


r = requests.get("https://www.ustapideci.com.tr/kampanyalar-ve-promosyonlar#paket-servis-kampanyalari")
soup = BeautifulSoup(r.content, "html.parser")
baslik = soup.find_all("span", attrs={"class": "title"})
resim = soup.find_all("span", attrs={"class": "picture"})
sayfa = soup.find_all("article", attrs={"class": "campaign"})

for idx, (a, b, c) in enumerate(zip(baslik, resim, sayfa)):
    title = a.text.strip()
    img = b.find("img")
    if img is not None:
        img_url = img["src"]
        img_url_relative = img["src"]
        img_url_absolute = urljoin(r.url, img_url_relative)
    sayfa_url = c.find("a")
    if sayfa_url is not None:
        url_relative  = sayfa_url["href"]
        url_absolute = urljoin(r.url, url_relative)

    
    campaign_id = f"ustapideci_campaign_{idx}"

   
    data = {
        "Baslik": title,
        "ResimUrl": img_url_absolute,
        "SayfaUrl": url_absolute
    }
    db.collection("kampanyalar").document(campaign_id).set(data)


r = requests.get("https://www.arbys.com.tr/kampanyalar-ve-promosyonlar#paket-servis-kampanyalari")
soup = BeautifulSoup(r.content, "html.parser")
baslik = soup.find_all("h2", attrs={"class": "title"})
resim = soup.find_all("figure", attrs={"class": "picture"})
sayfa = soup.find_all("figure", attrs={"class": "picture"})

for idx, (a, b, c) in enumerate(zip(baslik, resim, sayfa)):
    title = a.text.strip()
    img = b.find("img")
    if img is not None:
        img_url = img["src"]
        img_url_relative = img["src"]
        img_url_absolute = urljoin(r.url, img_url_relative)
    sayfa_url = c.find("a")
    if sayfa_url is not None:
        url_relative  = sayfa_url["href"]
        url_absolute = urljoin(r.url, url_relative)

    
    campaign_id = f"arbys_campaign_{idx}"

    
    data = {
        "Baslik": title,
        "ResimUrl": img_url_absolute,
        "SayfaUrl": url_absolute
    }
    db.collection("kampanyalar").document(campaign_id).set(data)
