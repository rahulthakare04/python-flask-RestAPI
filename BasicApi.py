from flask import Flask
from flask_restful import Resource,Api 

app=Flask(__name__)
api=Api(app)

class rahul(Resource):
    def get(self):
        dic={
            'name':'rahul thakare',
            'age':'20',
            'college':'sipna college',
            'mobaile no':'8010525150',
            'weight':'72',
            'heaight':'182cm'
        }
        return dic

api.add_resource(rahul,'/rahul')
app.run(debug=True)


