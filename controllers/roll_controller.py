from flask_restful import Resource, request

from controllers.parsers import parse_args
from services.roll_service import RollService


class RollController(Resource):
    @parse_args
    def post(self):
        roll_service = RollService()
        result, repeats = roll_service.roll(request.json)
        return {'roll': {'result': result, 'repeats': repeats}}, 200
