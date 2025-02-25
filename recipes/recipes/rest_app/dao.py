from recipes.rest_app.models import Movie


class Movie:

    @staticmethod
    def get_all_movies():
        return Movie.objects.all()


class MoviesByGenre(Movie):

    @staticmethod
    def get_for_kids_allowed_movies():
        return Movie.get_all_movies().filter(is_for_kids_allwed=True)

    @staticmethod
    def get_all_serials():
        return Movie.get_all_movies().filter(genre="serial")

    @staticmethod
    def get_adult_serials():
        return MoviesByGenre.get_all_serials().filter(is_for_kids_allwed=False)

    @staticmethod
    def get_for_kids_serials():
        return MoviesByGenre.get_all_serials().filter(is_for_kids_allwed=True)
