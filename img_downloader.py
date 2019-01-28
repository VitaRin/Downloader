import requests, os
from bs4 import BeautifulSoup

url = input("Paste the image url: ")
html = requests.get(url).content

os.chdir("C:\\Users\\Maintenant Prêt!\\Pictures\\imag")
def dwnld(filename, extension):
    full_filename = filename + extension
    with open(full_filename,"wb") as f:
        f.write(html)

name = input("How would you like to name the picture? ")

if ".png" in url:
        extension = ".png"

if ".jpeg" in url:
        extension = ".jpeg"

if ".jpg" in url:
        extension = ".jpg"


dwnld(name, extension)