import json

from bs4 import BeautifulSoup

from Film import Film
from SearchDataSource import SearchDataSource

host_url = "https://fmovies.wtf"


def search_film(search_query):
    search_datasource = SearchDataSource()

    search_result = []

    search_op = search_datasource.get_search_result(search_query=search_query)
    search_doc = BeautifulSoup(search_op, "html.parser")

    film_list_result = search_doc.find_all("div", class_="filmlist")

    film_list_item_result = film_list_result[0].find_all_next("div", class_="item")
    print(film_list_item_result)
    for i in range(len(film_list_item_result)):
        film_list_item = film_list_item_result[i]

        quality = str(film_list_item.find_next("div", class_="quality").contents[0]).strip()
        title = film_list_item.find_next("a", class_="poster").get("title").strip()
        link = host_url + film_list_item.find_next("a", class_="poster").get("href").strip()
        poster = film_list_item.find_next("a", class_="poster").find_next("img").get("src").strip()
        # rating = film_list_item.find_next("span", class_="imdb").contents[1] ToDo: Add support for ratings later
        release_date = str(film_list_item.find_next("div", class_="meta").contents[0]).strip()
        runtime = str(film_list_item.find_next("div", class_="meta").contents[2]).strip()
        film_type = str(
            film_list_item.find_next("div", class_="meta").find_next("i", class_="type").contents[0]).strip()

        film = Film(quality, title, link, poster, release_date, runtime, film_type)

        search_result.append(film)

    json_output = json.dumps(search_result, default=lambda obj: obj.__dict__)

    return json_output


print(search_film(search_query="John Wick"))
