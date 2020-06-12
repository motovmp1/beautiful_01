import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print("teste")

# this is url que quero copiar
myurl = 'https://www.newegg.com/global/hk-en/p/pl?d=graphics+cards'
print(myurl)

# open connection para abrir a pagina web, grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")
# this is a title
print(page_soup.h1)

# this is a div
print(page_soup.p)

containers = page_soup.findAll("div", {"class": "item-container"})
print(len(containers))

# container = containers[0]
# print(container.a.img["title"])

filename = "products.csv"
f = open(filename, "w")

headers = "INDEX_NUMBER, BRAND\n "

f.write(headers)

for number, container in enumerate(containers):
    brand = container.a.img["title"]
    print(number, "Brand:" + brand)
    index = str(number)
    f.write(index + "," + brand.replace(",", "") + "\n")

f.close()
