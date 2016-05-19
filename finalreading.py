from bs4 import BeautifulSoup
import urllib2
import re


with open("urls_data_NEW", "r") as a_file:
    url_data = a_file.read().split("\n")
a = " http://www.saatchiart.com/"
for url in url_data:
    s = "http://www.saatchiart.com/art/Painting-Waiting-for-the-train/26898/2631810/view"
    web_page = urllib2.urlopen(s)
    page_text = web_page.read()
    soup = BeautifulSoup(page_text,"lxml")
    # tag1 = soup.find("div",{"class":"small-12 medium-6 large-12 columns art-meta"})
    # print(tag1.text)
    # tag2= soup.find("div",{"class":"small-12 medium-6 large-12 columns"})
    # print(tag2.text)
    title = soup.find("h3",{"itemprop":"name"})
    creator = soup.find("p",{"itemprop":"creator"}).a
    size = soup.find("p",{"class":"category-size"})
    # print(title.text)
    # print(creator.text)

    sizes = [re.search(r'[\d.]+', s.text).group() for s in size.find_all("span")]
    size_list = [float(x) for x in sizes]
    size_prod = reduce(lambda x, y: x*y, size_list)
    # print(sizes)
    # print(size_prod)
    # print(size_prod)
    price = soup.find('span',{"class":"price"})
    views = soup.find("div",{"class":"art-detail-stats"})
    view =re.search(r'[\d]+', views.text).group()
    favourites = soup.find("div",{"id":"favoriteCount"})
    print(view)
    print(favourites.text)
    # print(price.text.strip())