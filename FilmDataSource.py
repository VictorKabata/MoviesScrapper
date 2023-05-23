class FilmDataSource:

    def get_film_detail(self, film_url):
        with open("movie_result.html", "r") as result:
            return result.read()

        # result = requests.get(film_url)
        # return result.text
