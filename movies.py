import json
import requests

# http://www.omdbapi.com/?i=tt3896198&apikey=41f4f453
class movie:
    def __init__(self, tittle, director, anio, gender):
        self.tittle = tittle
        self.director = director
        self.anio = anio
        self.gender = gender

class coleccion_peliculas:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_tittle):
        for movie in self.movies:
            if movie.tittle == movie_tittle.tittle:
                print(f"la pelicula {movie_tittle.tittle} ya existe ")
                return
        if movie_tittle.anio < 1888:
            print(f"La pelicula {movie_tittle.tittle} no puede ser menor al 1888")
            return
        
        if movie_tittle.tittle == "":
            print("La pelicula no se puede agregar porque le falta titulo")
            return
        
        if movie_tittle.director == "":
            print(f"La pelicula {movie_tittle.tittle} no se puede agregar porque le falta un director")
            return

        self.movies.append(movie_tittle)
        print(f"La pelicula{movie_tittle.tittle} ha sido agregada con exito")
    
    def delete_movie(self, movie_to_delete):
        for movie in self.movies:
            if movie.tittle == movie_to_delete:
                self.movies.remove(movie)
                print(f"La pelicula {movie_to_delete} ha sido eliminada con exito")
                return
        
        # Si no se encuentra la pelicula
        print("La pelicula" + movie_to_delete + " No existe en la base de datos")

    def search_movie(self, search_movie):
        for movie in self.movies:
            if movie.tittle == search_movie:
                print(movie)
                print(f"La pelicula {search_movie} se hizo en el anio {movie.anio} por el autor {movie.director} y el genero es {movie.gender}")
                return
                                                                                                                
        # Si no se encuentra la pelicula
        print("La pelicula con el nombre" + search_movie + " no existe en la coleccion")
    
    def show_all_movies(self):
        # Ordenamiento ascendente o descendente
        self.movies.sort(key=lambda movie: movie.anio, reverse=not False)
        for movie in self.movies:
            print(f"La pelicula {movie.tittle} hecha por el director {movie.director} en el anio {movie.anio} y su genero es {movie.gender}")

    def show_all_movies_by_drama(self, gender_drama):
        found = False
        for movie in self.movies:
            if movie.gender == gender_drama:
                print(f"La pelicula {movie.tittle} fue encontrada por su genero {movie.gender}")
                found = True
        
        if not found:
            print(f"No se ha encontrado peliculas del genero {gender_drama}")

    def get_movie_data(self, title):
        baseurl = "http://www.omdbapi.com/"
        params_dic = {}
        params_dic["t"] = title
        params_dic["apikey"] = "41f4f453"
        complete_dates = requests.get(baseurl, params_dic)

        if complete_dates.status_code == 200:
            movie_data = complete_dates.json()
            #print(movie_data)
        else:
            print("Error")

        movie_tittle = movie_data.get('Title')
        movie_director = movie_data.get('Director')
        movie_year = movie_data.get('Year')
        movie_genre = movie_data.get('Genre').split(",")
        movie_to_search = movie(movie_tittle, movie_director, movie_year, movie_genre[0])
        print((movie_tittle, movie_director, movie_year, movie_genre[0]))
        #print("Esto es un test", movie_data.get('Title'), movie_data.get('Director'), movie_data.get('Year'), movie_data.get('Genre'))
        #print("Evaluemos lo que pasa aqui", movie_data.get('Genre'))
                
movie1 = movie("The Shawshank Redemption", "Frank Darabont", 1994, "Accion")
movie2 = movie("The Godfather", "Francis Ford Coppola", 1972, "Accion")
movie3 = movie("The Dark Knight", "Christopher Nolan", 2008, "Acción")

my_collection = coleccion_peliculas()

#
#my_collection.add_movie(movie1)
#my_collection.add_movie(movie2)
#my_collection.add_movie(movie3)
print("-=================================================-")
#my_collection.delete_movie("The Godfather")
#my_collection.search_movie("The Dark Knight2")
#my_collection.show_all_movies()
my_collection.get_movie_data("The Godfather")
#my_collection.show_all_movies_by_drama("Drama")