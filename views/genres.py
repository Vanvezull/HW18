
from flask_restx import Namespace, Resource

from models import GenresSchema, Genre

"""
Вьюшки и namecspace для Genre
"""

genre_ns = Namespace('genres')

@genre_ns.route('/') # Представление для получения всех жанров
class GenreView(Resource):
    def get(self):
        return GenresSchema(many=True).dump(Genre.query.all()), 200


@genre_ns.route('/<int:id>') # Представление для получения жанра по id
class GenreView(Resource):
    def get(self, id):
        return GenresSchema().dump(Genre.query.get(id)), 201