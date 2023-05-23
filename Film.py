class Film:

    def __init__(self, quality, title, description, link, poster, release_date, runtime, film_type):
        self.quality = quality
        self.title = title
        self.description = description
        self.link = link
        self.poster = poster
        self.release_date = release_date
        self.runtime = runtime
        self.film_type = film_type

    def __str__(self):
        return f"Film(quality={self.quality}, title={self.title}, description={self.description},link={self.link}, poster={self.poster}, release_date={self.release_date}, runtime={self.runtime}, type={self.film_type})"
