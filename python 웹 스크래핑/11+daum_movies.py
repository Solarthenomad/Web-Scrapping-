import re
import requests
from bs4 import BeautifulSoup

url = ""

headers = {"user-agent" : ""}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img" , attrs = {"class" : "thumb_img"})

for image in images :
    #print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url
        
    print(image_url)
    
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    
    with open("movie{}.jpg".format(idx+1),"wb") as f:
        f.write(image_res.content)
        
    
