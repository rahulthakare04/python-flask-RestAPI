from flask import  Flask,jsonify
from flask_restful import Resource,Api
from pymongo import MongoClient



app=Flask(__name__)
api=Api(app)

class Book(Resource):

    def get(self):
        client=MongoClient("mongodb+srv://rahuldb:rahul123@rahulcluster.vviud.mongodb.net/?retryWrites=true&w=majority&appName=rahulcluster")
        db=client["marvel_projectdb"]
        coll=db["books"]
        lst=list(coll.find())
        lst1=[]
        for doc in lst:
            doc.pop('_id')
            print(doc)
            lst1.append(doc)
        jsoinlist=[doc for doc in lst1]  
        return jsonify(jsoinlist)  

api.add_resource(Book,"/books/all")  
app.run(debug=True)      