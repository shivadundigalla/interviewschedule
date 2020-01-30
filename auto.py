from flask import Flask, request,render_template
from pymongo import MongoClient
app=Flask(__name__)
client = MongoClient("mongodb+srv://abc:abcdefghi@cluster0-6kppu.mongodb.net/test?retryWrites=true&w=majority")
db = client["password1"]
mycol = db["details1"]


mycol2= db["details2"]


def func(s):
    x1=mycol.find({"username":s})
    for i in x1:
        return(i["password"])

@app.route('/validate1',methods=['POST'])
def getvalue():
    data=request.json

    pwds=data["password"]
    name=data["name"]
    if(pwds==func(name)):
        return({"status":"valid"})
    else:
        return ({"status":"invalid"})

@app.route('/validate2',methods=['POST'])
def getvalu():
    data=request.json
    num=data["idnum"]
    print(num)
    x1 = mycol2.find({"date": str(num)})
    if(len(list(x1))!=0):
        return({"status":"valid","slots":list(x1["slots"])})
    else:
        return ({"status":"invalid"})


@app.route('/')
def index():
    return render_template("candidate login.html")
@app.route('/css')
def index1():
    return render_template("csscalender.html")
if __name__=="__main__":
    app.run(debug=True)