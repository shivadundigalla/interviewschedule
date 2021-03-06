from flask import Flask, render_template, request, session,jsonify
from flask_jwt_extended import (
JWTManager, jwt_required, create_access_token,
get_jwt_identity
)
import csv
from json import dumps
import smtplib
import random
from werkzeug import secure_filename
from pymongo import MongoClient
pending=[]
reported=[]
fixed=[]
client = MongoClient("mongodb+srv://dbuser:1234@cluster0-hi2xt.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["login"]
mycol = db["candidate"]
db2 = client["Interviewer"]
mycol3 = db2["fixed"]

db = client["login"]
mycol2= db["hrlogin"]

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='/'
app.config['MAX_CONTENT_PATH']=1024*1024*1024*1024
def sendmail(name,mailid,text):

    s = smtplib.SMTP('smtp.gmail.com', 587)
    print(name,mailid)
    s.starttls()
    s.login("shiva.darwinbox@gmail.com", "Abcd@1234")
    p=random.randint(123456789,999999999)
    details= {
        "username":mailid,
        "password":str(p),
        "status":"pending"
    }
    mycol.insert_one(details)
    m="""This is a random message generated by us.Please visit the link to book your slot.
          https://google.com"""
    message="Hello "+str(name)+"\n"+"Thank you \n"+str(text)+"\nUsername is "+mailid+"\npassowrd is "+str(p)+"\n"
    message=message+m
    print(str(message))
    s.sendmail("shiva.darwinbox@gmail.com", mailid, message)
    print("DONE")
    s.quit()


def f1(file,text):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                sendmail(row[0],row[3],text)
                line_count += 1
def func(s):
    x1=mycol2.find({"username":s})
    for i in x1:
        return(i["password"])

@app.route('/')
def index1():
    
    return render_template("candidate login.html")


@app.route('/validate',methods=['POST'])
def getvalue():
    data=request.json

    pwds=data["password"]
    name=data["name"]
    if(pwds==func(name)):
        return({"status":"valid"})
    else:
        return ({"status":"invalid"})



@app.route('/file')
def index():
    try:
      global  pending
      pending= list(db.candidate.find({"status": "pending"}))

    except Exception as e:
        return dumps({'error': str(e)})

    try:
        global fixed
        fixed = list(mycol3.find({"year": "2020"}))

    except Exception as e:
        return dumps({'error': str(e)})

    try:
        global reported
        reported = list(db.candidate.find({"status": "done"}))

    except Exception as e:
        return dumps({'error': str(e)})
    return render_template("files.html",pending=pending,reported=reported,fixed=fixed)


@app.route('/adi',methods=["GET","POST"])
def f():
    file1=request.files["myFile"]
    text=request.form["area"]
    print(text)
    file1.save(secure_filename(file1.filename))
    print(type(file1))
    f1(file1.filename,text)
    global pending
    global reported
    global  fixed
    print(pending,reported,fixed)
    return render_template("files.html",pending=pending,reported=reported,fixed=fixed)


if __name__=="__main__":
    app.run(debug=True)