import json
from bs4 import BeautifulSoup
import requests

page = requests.get("https://open.spotify.com/artist/6ydoSd3N2mwgwBHtF6K7eX")

print(page.status_code)
# print(page.content)

# Open up source code and pip to BeautifulSoup
# with open('sourcecode.html', 'r') as f:
#   soup = BeautifulSoup(f, features='html.parser')

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

""""ALBUMS"""

# Find the h2 tag that has Albums heading
albumTag = soup.find('h2', string='Albums')

# Find the parent section of the h2 tag
albumSection = albumTag.find_parent('div')

# Find all list items within the section tag
albums = albumSection.findAll('div', {"data-testid":"card-mwp"})

# albums = albums.find('div')

# Iterate through scrape data and extract data
# album = albums[3]

allAlbumDetails = []
for album in albums:

  # Find album link
  aTag = album.find('a')
  albumLink = aTag['href']

  # Find album image
  albumDiv = aTag.find('div')
  albumImg = albumDiv.find('img')
  albumSrc = albumImg['src']

  # Find album name
  albumName = aTag.find('span').string

  # Find album year
  albumYear = aTag.findAll('div')
  albumYear = albumYear[1].string

  # print(albumYear, albumLink, albumName, albumSrc, sep='\n')

  albumDetails = {
    'name':albumName,
    'link':albumLink,
    'image':albumSrc,
    'year':albumYear
  }

  allAlbumDetails.append(albumDetails)

# print(albumDetails)

# extract data to json\
with open('albums.json', 'w') as a:
  json.dump(allAlbumDetails, a)



""""MONTHLY VIEWERS"""

listeners = soup.find('div', {"data-testid":"monthly-listeners-label"}).string

monthly_listeners = [
  listeners
]


"""POPULAR SONGS"""
# Find the h2 tag that has Albums heading
popularTag = soup.find('span', string='Popular')

# Find the parent section of the h2 tag
popularSection = popularTag.find_parent('div')

# Find all list items within the section tag
populars = popularSection.findAll('div', {"class":"EntityRowV2__Container-sc-ayafop-0"})

# Iterate through scrape data and extract data

allpopularDetails = []
for popular in populars:

  # Find popular Song Viewers
  aTag = popular.find('div')
  aTag = aTag.find('div')
  popularSongViewers = aTag.findAll('span')[2].string

  # Find popular song name
  popularSongSpans = aTag.findAll('span')[1]
  aSpanTag = popularSongSpans.find('a')
  popularSongName = popularSongSpans.find('a').string

  # find popular song link
  popularSongLink = aSpanTag['href']

  popularSongDetails = {
    'popular_song_name':popularSongName,
    'popular_song_link':popularSongLink,
    'popular_song_viewers':popularSongViewers,
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