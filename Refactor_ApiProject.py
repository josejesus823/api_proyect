import json
import requests

def get_movies_from_tastedive(name_movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {"q": name_movie, "type": "movies", "limit": 5}
    response_data= requests.get(baseurl, params = params_diction)
    name_movie = json.loads(response_data.text)
    return name_movie

def extract_movie_titles(movies_titles):
    movies_titles = [movie_name["Name"] for movie_name in movies_titles["Similar"]["Results"]]
    return movies_titles

def get_related_titles(movies):
    lst_all_movies = []
    for lista_movies in movies:
        dict_movies = get_movies_from_tastedive(lista_movies)
        lst_movies = extract_movie_titles(dict_movies)
        lst_all_movies += [movie for movie in lst_movies if movie not in lst_all_movies]
    return lst_all_movies

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    params_dic = {"apikey": "92da6e74", "t": title, "r": "json"}
    complete_dates = requests.get(baseurl, params_dic)
    name_movies = json.loads(complete_dates.text)
    return name_movies

def get_movie_rating(title_movies):
    info_rating = title_movies["Ratings"]
    rating = 0
    for rate in info_rating:
        if rate["Source"] == "Rotten Tomatoes":
            rating = int(rate["Value"][0:2])
    return rating    

def get_sorted_recommendations(names): 
	movies = get_related_titles(names) 
	mv_tuples = [] 
	for name in movies: 
		imbd = get_movie_data(name) 
		rotten = get_movie_rating(imbd) 
		record = (rotten, name) 
		mv_tuples.append(record) 
	mv_sort = sorted(mv_tuples, reverse=True) 
	return [mv[1] for mv in mv_sort]
        
print(get_sorted_recommendations(["Men in Black", "Black Swan"]))
