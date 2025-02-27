from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class FootballPlayers(Resource):
    def get(self,nat):
        lst=[]
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("select * from football_players where nationality='%s'"%nat)
        data=curs.fetchall()
        con.close()
        for rec in data:
            dic={}
            dic["name"]=rec[1]
            dic["age"]=rec[2]
            dic["nationality"]=rec[3]
            dic["club"]=rec[4]
            dic["position"]=rec[5]
            dic["goles"]=rec[6]
            lst.append(dic)
        return lst    

api.add_resource(FootballPlayers,"/player/<string:nat>")
app.run(debug=True,port=5001)
