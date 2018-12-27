from flask_restful import Resource


class TestController(Resource):

    def post(self):
        return {'Hey, look what I\'ve found!': 'Congratulations!!'}, 200
