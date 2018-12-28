#!flask/bin/python
from flask import Flask, request
from flask_restful import Api, Resource
from controllers import test_controller, roll_controller


app = Flask(__name__)
api = Api(app=app)
api.add_resource(test_controller.TestController, '/test')
api.add_resource(roll_controller.RollController, '/roll')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

