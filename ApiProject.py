import json
import requests


def get_movies_from_tastedive(name_movie):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = name_movie
    params_diction["type"] = "movie"
    params_diction["limit"] = 5
    response_data= requests.get(baseurl, params = params_diction)
    print(response_data.url)
    name_movie = json.loads(response_data.text)
    return name_movie

def extract_movie_titles(movies_titles):
    results_movies = movies_titles["Similar"]["Results"]
    movies_titles = []
    for movies_name in results_movies:
        movies_titles.append(movies_name["Name"])
    return movies_titles

def get_related_titles(movies):
    lst_all_movies = []
    for lista_movies in movies:
        dict_movies = get_movies_from_tastedive(lista_movies)
        lst_movies = extract_movie_titles(dict_movies)
        for pta in lst_movies:
            if pta not in lst_all_movies:
                lst_all_movies.append(pta)
    return lst_all_movies

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    params_dic = {}
    params_dic["r"] = "json"
    params_dic["t"] = title
    #complete_dates = requests_with_caching.get(baseurl, params_dic)
    complete_dates = requests.get(baseurl, params_dic)
    name_movies = json.loads(complete_dates.text)
    return name_movies

def get_movie_rating(title_movies):
    info_movie = title_movies
    info_rating = info_movie["Ratings"]
    rating = 0
    for pt in info_rating:
        if pt["Source"] == "Rotten Tomatoes":
            rating = int(pt["Value"][0:2])
    return rating

def get_sorted_recommendations(movies):
    dic_mov = {}
    lst_movies = []
    lst_movies2 = []
    titles_movies = get_related_titles(movies)
    for title_mv in titles_movies:
        rating = get_movie_rating(get_movie_data(title_mv))
        dic_mov[title_mv] = rating
    sort_orders = sorted(dic_mov.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for mv, rate in sort_orders:
        if rate == 0:
            lst_movies.append(mv)
            lst_movies = sorted(lst_movies, reverse=True)
        else:
            lst_movies2.append(mv)
    last_result = lst_movies2 + lst_movies
    return last_result
   
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

#print(extract_movie_titles(get_movies_from_tastedive("Men in Black")))