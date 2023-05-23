class SearchDataSource:

    def get_search_result(self, search_query):
        self.search_query = search_query

        url = "https://fmovies.wtf/search?keyword=" + search_query + "&vrf=R7Kdeg9L%2B54CAw%3D%3D"

        with open("result.html", "r") as result:
            return result.read()

        # result = requests.get(url)
        # return result.text
