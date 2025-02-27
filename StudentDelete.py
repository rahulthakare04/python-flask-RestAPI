from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route("/student/delete",methods=['DELETE'])
def deleteStudent():
    sid=int(request.form.get('student_id'))
    dic={}
    try:
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        student=curs.execute("select * from student where student_id=%d"%sid)
        if student:
            curs.execute("delete from student where student_id=%d"%sid)
            con.commit()
            dic["status"]="student delete succsefully "
        else:
            dic["status"]="student not found"
    except Exception as e:
        dic['status']=f"delete fail {e}"
    return dic

app.run(debug=True)