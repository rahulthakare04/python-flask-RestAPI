from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class movie(Resource):
    def get(self,release_year):
        rel=float(release_year)
        lst=[]
        
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("SELECT * FROM movie_sequence WHERE release_year =%d"%rel)
        data=curs.fetchall()
        for rec in data:
            dic={}
            dic["name"]=rec[1]
            dic["release_year"]=rec[2]
            dic["derecter"]=rec[3]
            dic["IMDB_rating"]=float(rec[4])
            print(dic)
            lst.append(dic)
            print(lst)
        return lst
api.add_resource(movie,"/movie/search/<release_year>")
app.run(debug=True)