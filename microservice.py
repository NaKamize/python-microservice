from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

movie_parser = reqparse.RequestParser()
movie_parser.add_argument(
    "title", type=str, help="Title of the movie is missing ...", required=True)
movie_parser.add_argument("description", type=str,
                          help="Description of the movie.")
movie_parser.add_argument("release_year", type=int,
                          help="Release year of the movie is missing ...", required=True)

movies = []


def wrong_id(id):
    if not next((item for item in movies if item["id"] == id), None):
        abort(404, message="Invalid movie ID!")


def ret_format(id):
    return [movie for movie in movies if movie['id'] == id]


class Movie(Resource):
    def get(self, id):
        wrong_id(id)
        return ret_format(id)

    def put(self, id):
        wrong_id(id)
        args = movie_parser.parse_args()
        for movie in movies:
            if movie['id'] == id:
                movie['title'] = args['title']
                movie['release_year'] = args['release_year']
                if args['description'] is not None:
                    movie['description'] = args['description']

        return ret_format(id), 201


class Movies(Resource):
    def get(self):
        return movies

    def post(self):
        args = movie_parser.parse_args()
        id_d = {"id": None}
        if len(movies) == 0:
            id_d["id"] = 1
        else:
            id_d["id"] = movies[-1]['id'] + 1
        id_d.update(args)
        movies.append(id_d)
        return args, 201


api.add_resource(Movies, "/movies")
api.add_resource(Movie, "/movies/<int:id>")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8000"))
