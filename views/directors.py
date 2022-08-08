
from flask_restx import Namespace, Resource

from models import DirectorSchema, Director
"""
Вьюшки и namecspace для Director
"""

director_ns = Namespace('directors')


@director_ns.route('/')  # Представление для получения всех режиссеров
class DirectorView(Resource):
    def get(self):
        return DirectorSchema(many=True).dump(Director.query.all()), 200


@director_ns.route('/<int:id>')  # Представление для получения режиссера по id
class DirectorView(Resource):
    def get(self, id):
        return DirectorSchema().dump(Director.query.get(id)), 201
