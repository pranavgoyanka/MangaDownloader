# manga downloader from manga panda
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import os.path
ch = 1 
page = 1
print(os.getcwd())
baseAdd = input("Enter the base address of your manga from MangaPand\neg: https://www.mangapanda.com/shingeki-no-kyojin/\nBase Address: ")
inich = int(input("Enter Initial Chapter Number: "))
finch = int(input("Enter Final Chapter Number: "))
skip = input("Overwrite existing files? (y/n):")
print(skip)
fin = 2;
ch = inich
if os.path.isdir("." + baseAdd[26:]) == False:
    os.mkdir("."+baseAdd[26:])    

os.chdir("." + baseAdd[26:])

for ch in range(inich,  finch+1):

    if os.path.isdir("./" + str(ch)) == False:
        os.mkdir("./"+str(ch))    

    os.chdir("./"+str(ch))

    url = baseAdd + str(ch)
    url
    r = requests.get(url)
    r.content
    soup = BeautifulSoup(r.content);
    fin = int(soup.find_all("option")[-1].get_text())

    print("Chapter", ch, ": is stored at ", os.getcwd())
    for i in tqdm(range(1, fin + 1), desc="Chapter " + str(ch), ascii = True):
        if all([os.path.isfile(str(page) + ".jpg") == False]):
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