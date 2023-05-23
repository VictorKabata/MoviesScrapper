import json

from bs4 import BeautifulSoup

from Film import Film
from FilmDataSource import FilmDataSource
from FilmDetail import FilmDetail
from SearchDataSource import SearchDataSource

host_url = "https://fmovies.wtf"


def search_film(search_query):
    search_datasource = SearchDataSource()

    search_result = []

    search_op = search_datasource.get_search_result(search_query=search_query)
    search_doc = BeautifulSoup(search_op, "html.parser")

    film_list_result = search_doc.find_all("div", class_="filmlist")[0].find_all_next("div", class_="item")

    for i in range(len(film_list_result)):
        film_list_item = film_list_result[i]

        quality = film_list_item.find_next("div", class_="quality").text
        title = film_list_item.find_next("a", class_="poster").get("title")
        link = host_url + film_list_item.find_next("a", class_="poster").get("href")
        poster = film_list_item.find_next("a", class_="poster").find_next("img").get("src")
        release_date = str(film_list_item.find_next("div", class_="meta").contents[0]).strip()
        runtime = str(film_list_item.find_next("div", class_="meta").contents[2]).strip()
        film_type = film_list_item.find_next("i", class_="type").text
        description = ""  # ToDo: Get description

        film = Film(quality, title, description, link, poster, release_date, runtime, film_type)

        search_result.append(film)

    json_output = json.dumps(search_result, default=lambda obj: obj.__dict__)

    return json_output


def get_film_detail(film_url):
    film_datasource = FilmDataSource()

    get_film_detail_op = film_datasource.get_film_detail(film_url=film_url)
    film_detail_doc = BeautifulSoup(get_film_detail_op, "html.parser")

    title = film_detail_doc.find("h1", class_="title").text
    description = film_detail_doc.find("div", class_="desc shorting").text
    poster = film_detail_doc.find("div", class_="poster").find("img").get("src")
    quality = film_detail_doc.find("span", class_="quality").text
    link = film_url
    release_date = film_detail_doc.find("span", itemprop="dateCreated").text
    film_type = film_detail_doc.find("i", class_="type").text
    runtime = film_detail_doc.find("div", class_="meta").contents[5].text
    similar_movies = []

    # ToDo: Get similar movies
    # similar_films = film_detail_doc.find("div", class_="filmlist")
    # for similar_film in similar_films:
    #     quality = similar_film.find_next("div", class_="quality").text
    #     title = similar_film.find_next("a", class_="title").get("title")
    #     link = similar_film.find_next("a", class_="title").get("href")
    #     poster = similar_film.find_next("a", class_="poster").find("img").get("src")
    #     release_date = str(similar_film.find_next("div", class_="meta").contents[0]).strip()
    #     runtime = str(similar_film.find_next("div", class_="meta").contents[2]).strip()
    #     film_type = similar_film.find_next("div", class_="meta").find_next("i", class_="type").text
    #
    #     similar_film = Film(quality, title, description, link, poster, release_date, runtime, film_type)
    #     similar_movies.append(similar_film)
    #
    # print(similar_movies)

    film_detail = FilmDetail(quality, title, description, link, poster, release_date, runtime, film_type,
                             similar_movies)

    json_output = json.dumps(film_detail, default=lambda obj: obj.__dict__)

    return json_output


print(search_film(search_query="Terminator"))
print(get_film_detail(film_url="https://fmovies.wtf/movie/john-wick-npnn"))
