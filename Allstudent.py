from flask import Flask
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

class Students(Resource):
    def get(self):
        lst = []
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs = con.cursor()
        curs.execute("select * from student")
        data = curs.fetchall()
        con.close()
        
        for rec in data:
            dic = {
                "student_id": rec[0],
                "first_name": rec[1],
                "last_name": rec[2],
                "age": rec[3],
                "grade": rec[4],
                "gender": rec[5]
            }
            lst.append(dic)
            
        return lst

api.add_resource(Students, "/students/all")
app.run(debug=True,port=5002)

