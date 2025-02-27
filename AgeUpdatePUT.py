from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route("/student/ageupdate",methods=['PUT'])
def updateAge():
    sid=int(request.form.get("student_id"))
    age=int(request.form.get('age'))
    dic={}
    try:
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("update student set age=%d where student_id=%d" %(age,sid))
        con.commit()
        con.close()
        dic["status"]="age updated"
    except:
        dic["status"]="age not update"
    return dic

app.run(debug=True)