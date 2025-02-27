from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class Movie(Resource):
    def get(self,nm):
        
        dic={}
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("SELECT * FROM movie_sequence WHERE movie_name ='%s'"%nm)
        data=curs.fetchone()
       
        if data:
            dic["name"]=data[1]
            dic["release_year"]=data[2]
            dic["derecter"]=data[3]
            dic["IMDB_rating"]=float(data[4])
        else:
            dic["name"]="not found"
            dic["release_year"]="not found"
            dic["derecter"]="not found"
            dic["IMDB_rating"]="not found"
        con.close()
        return dic
api.add_resource(Movie,"/movie/search/<string:nm>")
app.run(debug=True)
