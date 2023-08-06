#problem 1:
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

#problem 2:
import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])

#problem 3:
import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    param = {"q": movie, "limit": 5, "type": "movies"}
    tastedive_response = requests_with_caching.get(baseurl, params = param)
    return json.loads(tastedive_response.text)

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")


#problem 4:
import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    param = {"q": movie, "limit": 5, "type": "movies"}
    tastedive_response = requests_with_caching.get(baseurl, params = param)
    return json.loads(tastedive_response.text)
def extract_movie_titles(dic):
    return [dic['Name'] for dic in dic['Similar']['Results']]

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

#problem 5:
import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params = {"q": movie, "limit": 5, "type": "movies"}
    tastedive_response = requests_with_caching.get(baseurl, params=params)
    return json.loads(tastedive_response.text)

def extract_movie_titles(response):
    return [result['Name'] for result in response['Similar']['Results']]

def get_related_titles(movie_list):
    related_titles = []
    for movie in movie_list:
        response = get_movies_from_tastedive(movie)
        titles = extract_movie_titles(response)
        related_titles.extend(titles)
    return list(set(related_titles))

print(get_related_titles(["Black Panther", "Captain Marvel"]))
print(get_related_titles([]))

#problem 6:
import requests_with_caching
import json

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    param = {"t": title, "r": "json"}
    omdb_response = requests_with_caching.get(baseurl, params=param)
    return json.loads(omdb_response.text)

get_movie_data("Venom")
get_movie_data("Baby Mama")

#problem 7:
import requests_with_caching
import json

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    param = {"t": title, "r": "json"}
    omdb_response = requests_with_caching.get(baseurl, params=param)
    return json.loads(omdb_response.text)

def get_movie_rating(dic):
    ranking = dic['Ratings']
    for item in ranking:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0

get_movie_rating(get_movie_data("Deadpool 2"))

#problem 8:
import requests_with_caching
import json

import requests_with_caching
import json


def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params = {"q": movie, "limit": 5, "type": "movies"}
    tastedive_response = requests_with_caching.get(baseurl, params=params)
    return json.loads(tastedive_response.text)


def extract_movie_titles(response):
    return [result['Name'] for result in response['Similar']['Results']]


def get_related_titles(movie_list):
    related_titles = []
    for movie in movie_list:
        response = get_movies_from_tastedive(movie)
        titles = extract_movie_titles(response)
        related_titles.extend(titles)
    return list(set(related_titles))


def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    param = {"t": title, "r": "json"}
    omdb_response = requests_with_caching.get(baseurl, params=param)
    return json.loads(omdb_response.text)


def get_movie_rating(dic):
    ranking = dic['Ratings']
    for item in ranking:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0


def get_sorted_recommendations(movie_list):
    related_titles = get_related_titles(movie_list)
    movie_data = [get_movie_data(movie) for movie in related_titles]
    return sorted(movie_data, key=lambda movie: (get_movie_rating(movie), movie['Title']), reverse=True)

# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
