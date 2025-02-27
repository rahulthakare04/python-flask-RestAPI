from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/student/add',methods=['POST'])
def newStudent():
    sid=int(request.form.get('student_id'))
    fnm=request.form.get('first_name')
    lnm=request.form.get('last_name')
    age=int(request.form.get('age'))
    gd=request.form.get('grade')
    gen=request.form.get('gender')
    dic={}
    try:
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("insert into student (student_id,first_name,last_name,age,grade,gender) values (%d,'%s','%s',%d,'%s','%s')"%(sid,fnm,lnm,age,gd,gen))
        con.commit()
        con.close()
        dic["status"]="new student add"
    except:
        dic["status"]="fail"
    return dic


app.run(debug=True)
