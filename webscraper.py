from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# Create a list of the top movies
top_movies = []

# Loop through the list of top movies and parse through data
for movie in content.find_all('tbody', attrs={"class": "lister-list"}):
	for movieRow in content.find('tr'):
		movieObject = {
			# Hold off on grabbing the movie posters, might interfere with collecting data
			 #"poster": movie.find('td', attrs={"class": "posterColumn"}).text,
			"title": movie.find('a').next_sibling,
			"year": movie.find('span', attrs={"class": "secondaryInfo"}).text,
			"rating": movie.find('td', attrs={"class": "imdbRating"}).text,
		}
	print(movieObject)
	#print("==========Text Results==========")
	#print(movieObject.get_text())

