# manga downloader from manga panda
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
import progressbar
import os
from progressbar import ProgressBar
ch = 1 #chapter
page = 1

# k = input("Press any key to proceed...")
    
baseAdd = input("Enter the base address of your manga from MangaPand\neg: https://www.mangapanda.com/shingeki-no-kyojin/\nBase Address: ")
inich = int(input("Enter Initial Chapter Number: "))
finch = int(input("Enter Final Chapter Number: "))
# fin = int(input("Enter last page number of chapter: "))
# fin = int(soup.find_all("option")[-1].get_text())
fin = 2;
ch = inich
for ch in range(ch,  finch+1):
    if os.path.isdir(baseAdd[26:]) == False:
        os.mkdir(baseAdd[26:])    

    os.chdir(baseAdd[26:])
    if os.path.isdir(str(ch)) == False:
        os.mkdir(str(ch))    

    os.chdir(str(ch))

    url = baseAdd + str(ch)
    r = requests.get(url)
    r.content
    soup = BeautifulSoup(r.content);
    time.sleep(2)
    fin = int(soup.find_all("option")[-1].get_text())

    for i in range(1, fin + 1):
        url = baseAdd + str(ch) + "/" + str(page)
        r = requests.get(url)
        r.content
        soup = BeautifulSoup(r.content);
        imgurl = soup.find_all("img", {"id":"img"})
        imgurls = str(imgurl)
        start = imgurls.find('src=\"') + 5
        end = imgurls.find('.jpg') + 4
        imgurls = imgurls[start:end]
        # print(imgurls)
        class AppURLopener(urllib.request.FancyURLopener):
            version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
        urllib._urlopener = AppURLopener()
        urllib._urlopener.retrieve(imgurls, str(page) + ".jpg")
        page = page + 1
    os.chdir('..')
    page = 1

k = input("Press any key to exit...")