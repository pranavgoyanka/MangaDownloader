# manga downloader from manga panda
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
ch = 1 #chapter
page = 1

# k = input("Press any key to proceed...")
    
# baseAdd = input("Enter the base address of your manga from MangaPand\neg: https://www.mangapanda.com/shingeki-no-kyojin/\nBase Address: ")

baseAdd = "https://www.mangapanda.com/shingeki-no-kyojin/"


for i in range(1, 58):
    url = baseAdd + str(ch) + "/" + str(page)

    # k = input("Press any key to proceed...")

    r = requests.get(url)
    r.content
    # k = input("Press any key to proceed...")
    soup = BeautifulSoup(r.content);

    imgurl = soup.find_all("img", {"id":"img"})
    imgurls = str(imgurl)
    start = imgurls.find('src=\"') + 5
    end = imgurls.find('.jpg') + 4
    imgurls = imgurls[start:end]
    print(imgurls)
    # k = input("Press any key to proceed...")
    # time.sleep(2)
    # print img.a['href'].split("imgurl=")[1]
    # urllib.request.urlretrieve(imgurls, str(page) + ".jpg")

    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
    urllib._urlopener = AppURLopener()

    urllib._urlopener.retrieve(imgurls, str(page) + ".jpg")
    page = page + 1
k = input("Press any key to exit...")