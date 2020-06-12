import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print("teste")

# this is url que quero copiar
myurl = 'https://campinascomprelocal.com.br/tipo/bebidas/'
print(myurl)

# open connection para abrir a pagina web, grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")
# this is a title
print(page_soup.title)

# this is a div
print(page_soup.p)


containers = page_soup.findAll("div", {"class": "elementor-widget-container"})
print(len(containers))

container = containers
# print(container)


filename = "bebidas.txt"
f = open(filename, "w")

for tag in container:
    print(tag.text)
    f.write(tag.text + "\n")

f.close()