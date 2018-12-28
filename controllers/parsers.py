from functools import wraps

from flask_restful import reqparse


def parse_args(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('author', required=True, help='¿Quién está haciendo esa tirada? Falta el campo author.')
        parser.add_argument('dices', required=True, type=int, help='El campo dices es obligatorio y tiene que ser'
                                                                   ' un número para indicar el número de dados'
                                                                   ' que se lanzan')
        parser.add_argument('diceType', type=int, help="El campo debe ser un número para "
                                                       "indicar el número de caras de los dados que se tiran.")
        params = parser.parse_args(strict=True)

        return f(*args, **kwargs)

    return decorated_function
