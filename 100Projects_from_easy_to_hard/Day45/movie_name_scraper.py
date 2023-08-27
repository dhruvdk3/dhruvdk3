from bs4 import BeautifulSoup
import requests
from pprint import pprint
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_data = response.text
soup = BeautifulSoup(web_data, 'html.parser')
data = soup.find_all(name='h3', class_="title")
movie = [i.string for i in data]
movie.reverse()

with open("movies.txt", mode="w") as file:
    for i in movie:
        file.write(i+'\n')