# manga downloader from manga panda
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
import os
ch = 1 #chapter
page = 1

# k = input("Press any key to proceed...")
    
# baseAdd = input("Enter the base address of your manga from MangaPand\neg: https://www.mangapanda.com/shingeki-no-kyojin/\nBase Address: ")

baseAdd = "https://www.mangapanda.com/shingeki-no-kyojin/"
ch = int(input("Enter Chapter Number: "))
end = int(input("Enter last page number of chapter: "))

# for ch in range(1,  112):
os.mkdir(str(ch))
os.chdir(str(ch))
for i in range(1, end + 1):
    url = baseAdd + str(ch) + "/" + str(page)
    r = requests.get(url)
    r.content
    soup = BeautifulSoup(r.content);
    imgurl = soup.find_all("img", {"id":"img"})
    imgurls = str(imgurl)
    start = imgurls.find('src=\"') + 5
    end = imgurls.find('.jpg') + 4
    imgurls = imgurls[start:end]
    print(imgurls)
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
    urllib._urlopener = AppURLopener()
    urllib._urlopener.retrieve(imgurls, str(page) + ".jpg")
    page = page + 1
    # os.chdir('..')

k = input("Press any key to exit...")