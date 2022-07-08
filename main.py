import json
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())

# website to scrape
website = ("https://open.spotify.com/artist/2jzc5TC5TVFLXQlBNiIUzE")

driver.get(website)
see_more_class ="//div[@class='Type__TypeElement-goli3j-0 dhAODk']"

see_more_element = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Type__TypeElement-goli3j-0 dhAODk']"))))

time.sleep(5)
body_html = driver.find_element(By.TAG_NAME, "html")
html = body_html.get_attribute('innerHTML')

soup=BeautifulSoup(html, 'html.parser')

# with open('test.html', 'w') as a:
#   json.dump(html, a)

# # page = requests.get("https://open.spotify.com/artist/2jzc5TC5TVFLXQlBNiIUzE")

# # print(page.status_code)
# # print(page.content)

# # Open up source code and pip to BeautifulSoup
# # with open('sourcecode.html', 'r') as f:
# #   soup = BeautifulSoup(f, features='html.parser')


# print(soup.prettify())

""""ALBUMS"""

# Find the h2 tag that has Albums heading
albumTag = soup.find('h2', string='Albums')

# Find the parent section of the h2 tag
albumSection = albumTag.find_parent('section')

# Find all list items within the section tag
albums = albumSection.findAll('div', {"draggable":"true"})
# albums = albums[2]
# ImgTag = albums.find('img')
# albumSrc = ImgTag['src']
# aTag = albums.find('a')
# albumLink = aTag['href']
# albumName = aTag['title']

# albums = albums.findAll('img', {"data-testid":"card-image"})
# print(albumName, albumLink, albumSrc)

# albums = albums.find('div')

# Iterate through scrape data and extract data
# album = albums[3]

allAlbumDetails = []
for album in albums:

  # Find album link
  ImgTag = album.find('img')
  albumSrc = ImgTag['src']
  aTag = album.find('a')
  albumLink = aTag['href']
  albumName = aTag['title']
  timeTag = album.find('time')
  albumYear = timeTag['datetime']

  albumDetails = {
    'name':albumName,
    'link':albumLink,
    'image':albumSrc,
    'year':albumYear
  }

  allAlbumDetails.append(albumDetails)

# print(allAlbumDetails)

# extract data to json\
# with open('albums.json', 'w') as a:
#   json.dump(allAlbumDetails, a)



""""MONTHLY VIEWERS"""

listeners = soup.find('div', {"class":"Type__TypeElement-goli3j-0 lpjVdv"}).string

monthly_listeners = [
  listeners
]


"""POPULAR SONGS"""
# Find the h2 tag that has Albums heading
popularTag = soup.find('h2', string='Popular')

# Find the parent section of the h2 tag
popularSection = popularTag.find_parent('div')

# # Find all list items within the section tag
populars = popularSection.findAll('div', {"role":"row"})

# populars = populars[9]
# ImgTag = populars.find('img')
# popularsSrc = ImgTag['src']
# popularsName = populars.find('div',{"dir":"auto"}).string
# popularsViewers = populars.find('div',{'class':"ebHsEf"}).string
# popularsLink = aTag['href']
# popularsName = aTag['title']
# timeTag = populars.find('time')
# popularsYear = timeTag['datetime']

# print(popularsSrc, popularsName,popularsViewers)

# # Iterate through scrape data and extract data

allpopularDetails = []
for popular in populars:

  ImgTag = popular.find('img')
  popularsSrc = ImgTag['src']
  popularsName = popular.find('div',{"dir":"auto"}).string
  popularsViewers = popular.find('div',{'class':"ebHsEf"}).string

  popularSongDetails = {
    'popular_song_name':popularsName,
    'popular_song_image':popularsSrc,
    'popular_song_viewers':popularsViewers,
  }

  allpopularDetails.append(popularSongDetails)


# extract data to json
with open('albums.json', 'w') as a:
  json.dump(allAlbumDetails, a)

with open('albums.json') as data_file:
    old_data = json.load(data_file)

data = old_data + monthly_listeners + allpopularDetails
with open('albums.json', 'w') as outfile:
    json.dump(data, outfile)

time.sleep(100)

driver.close