class SearchDataSource:

    def __init__(self):
        self.search_query = None

    def get_search_result(self, search_query):
        self.search_query = search_query

        query = str(search_query).replace(" ", "+")
        url = "https://fmovies.wtf/search?keyword=" + query + "&vrf=R7Kdeg9L%2B54CAw%3D%3D"

        with open("search_result.html", "r") as result:
            return result.read()

        # ToDo: Get data from real data source
        # result = requests.get(url)
        # return result.text
