from flask import Flask,render_template,request,jsonify,redirect,session,url_for,after_this_request
from datetime import timedelta
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,create_refresh_token
)
from flask_cors import CORS
from index import getName
from forone import forone
from start import start
from checkLifes import getLife
from subjectWise import subjectWise
from main import main
from stats import *
from newlnct import newlnct
from firebase import Firebase
from newlnctnotification import getAttendance
from cryptography.fernet import  Fernet
from redis import Redis
from rq import Queue
r = Redis()
q = Queue(connection=r)
from flask_sslify import SSLify
from dateWise import dateWise,getDateWiseAttendace
import os
config = {
    "apiKey": str(os.getenv('apiKey1')),
    "authDomain": "lnctdata.firebaseapp.com",
    "databaseURL": "https://lnctdata.firebaseio.com",
    "projectId": "lnctdata",
    "storageBucket": "lnctdata.appspot.com",
    "messagingSenderId": str(os.getenv('messageid1')),
    "databaseURL": "https://lnctdata.firebaseio.com"
}
firebase = Firebase(config)
db = firebase.database()
app = Flask(__name__,static_url_path='/static', template_folder="templates")
CORS(app)
app.config['JWT_SECRET_KEY'] = '9993929488@t'
jwt = JWTManager(app)
# SSLify(app)
app.secret_key = "9993929488@t"
@app.route("/logout",methods=['GET'])
def logout():
    try:
        print(session['username'])
        db.child(session['username']).update({
            'loggedout':'True'
        })
    except:
        print('error')
    session.pop('username',None)
    return  redirect("/")
@app.route('/getDateWiseAttendance',methods = ['GET'])
def dateWiseAttendance():
    if ('username' in request.args and "password" in request.args):
        if (request.args['username'] == "123" and request.args['password'] == "123"):
            response = getDateWiseAttendace("11156823968", "tushar#123")
        elif ('lnctu' in request.args):
            response = getDateWiseAttendace(request.args['username'], request.args['password'], True)
        else:
            response = getDateWiseAttendace(request.args['username'], request.args['password'])

        if response == "error":
            return "YOUR ID OR PASSWORD IS NOT CORRECT"
        else:
            return jsonify(response)
    else:
        return "Some parameters are missing"
@app.route("/attendance",methods = ["POST","GET"])
def attendance():
    if('username' in session):
        try:
            username = session['username']
            password = db.child(username+'/password').get().val()
            password = f.decrypt(password.encode()).decode()
            list = newlnct(username,password)
            if list == "error":
                session.pop('username',None)
                return render_template("error.html")
            else:
                print(list)
                return render_template("attendance.html",img=list[0],name=list[1],total=int(list[2]),present=int(list[3]))
        except:
            session.pop('username',None)
            return redirect("/")
    else:
        if request.method =="POST":
            session.permanent = True
            session['username'] = request.form['username']
            if('token' in session):
                db.child(request.form['username']).update({
                    'token':session['token']
                })
            list = newlnct(request.form['username'],request.form['password'])
            if list == "error":
                session.pop('username', None)
                return render_template("error.html")

            return render_template("attendance.html",img=list[0],name=list[1],total=list[2],present=list[3])
        elif request.method =="GET":
            return redirect("/")

@app.route('/env')
def env():
    import os;

    print(os.getenv('api'))
    return 'success'
@app.route("/getToken",methods =["POST"])
def getToken():
    data = request.get_json(force=True)
    if(data['username']!=None and data['password']!=None):
        response = getName(data['username'], data['password'],token='')
        if response == "error":
            return "YOUR ID OR PASSWORD IS NOT CORRECT"
        else:
            password = str(data['password']).encode()
            password = f.encrypt(password).decode()
            access_token = create_access_token(expires_delta=timedelta(days=60),identity={'username': data['username'],'password':password})
            apires = {
                "Name": response[1],
                "ImageUrl": response[0],
                "Semseter": response[3],
                "Branch": response[4],
                "College": response[2],
                "Section": response[5],
                'access_token' :access_token,

            }
            return jsonify(apires)
    else:
        return "Some parameters are missing"
@app.route('/getLifes')
def checkLifes():
    if('id' in request.args):
        return jsonify({'lifes':getLife(request.args['id'],True)})
    else:
        return jsonify({'error':'id is missing'})
@app.route("/api-bulk")
def bulk():
    if ('id'in request.args and 'startingCode' in request.args and 'semester' in request.args and 'start' in request.args):
        return jsonify(start(request.args['id'],request.args['startingCode'], request.args['semester'],int(request.args['start'])))
    else:
        return jsonify({
            "Error": 'Some Parameters are missing',
            "Reason": "You Must Enter RollNo ans semester"
        })
@app.route("/api",methods = ["GET","POST","PUT"])
def resultforone():
    if ('rollno' in request.args and 'semester' in request.args):
        if ('stream' in request.args):
            if(request.args['stream']!='0'):
                return jsonify({
                    'msg': 'Sorry this feture is currently not implemented for your stream'
                }
                )
        res = forone(request.args['rollno'], request.args['semester'])
        if (res == "Error"):
            return jsonify({
                "Error": "Result for this RollNo not found"
            })
        else:
            return jsonify({
                "Name":res[0],
                "CGPA":res[2],
                "SGPA":res[1],
                "data":res[3]

            })
    else:
        return jsonify({
            "Error": 'Some Parameters are missing',
            "Reason": "You Must Enter RollNo ans semester"
        })
#FOR WEB APP
#TO ENABLE IT PLEASE CHANGE THE ROUTE AS IT IS ALREADY IN USE
# @app.route("/api",methods=['POST'])
# @jwt_required
# def api():
#     data = get_jwt_identity()
#
#     password = data['password']
#     password = f.decrypt(str(password).encode())
#     response = main(data['username'], password.decode())
#     if (response == "error"):
#         return "YOUR ID OR PASSWORD IS NOT CORRECT"
#     else:
#         apires = {
#             "Name": response[0],
#             "Total Lectures": response[1],
#             "Present ": response[2],
#             "Percentage": response[3],
#             "Branch": response[4],
#             "College": response[5],
#             "Semester": response[6],
#             "LecturesNeeded": response[7],
#             'DaysNeeded': response[8]
#         }
#         return jsonify(apires)

@app.route("/login",methods =["POST","GET"])
def login():
    if(request.method=="POST"):
        data = request.get_json()
        if(data['username']!=None and data['password']!=None and data['token']!=None):
            response = getName(data['username'], data['password'], data['token'])
            if response == "error":
                return "YOUR ID OR PASSWORD IS NOT CORRECT"
            else:
                apires = {
                    "Name": response[1],
                    "ImageUrl": response[0],
                    "Semseter": response[3],
                    "Branch": response[4],
                    "College": response[2],
                    "Section": response[5]
                }
                return jsonify(apires)
        else:
            return "Some parameters are missing"
    else:
        if ('username' in request.args and "password" in request.args and 'token' in request.args):
            if(request.args['username']=="123" and request.args['password']=="123"):
                response = getName("11156823968", "tushar#123", "test")
            elif('lnctu' in request.args):
                response = getName(request.args['username'], request.args['password'],request.args['token'],True)
            else:
                response = getName(request.args['username'], request.args['password'], request.args['token'])
            if response == "error":
                return "YOUR ID OR PASSWORD IS NOT CORRECT"
            else:
                apires = {
                    "Name":response[1],
                    "ImageUrl":response[0],
                    "Semseter":response[3],
                    "Branch" :response[4],
                    "College":response[2],
                    "Section":response[5]
                }
                return jsonify(apires)
        else:
            return "Some parameters are missing"
@app.route("/send",methods=['GET'])
def sendNotification():
    if('password' in request.args):
        if(request.args['password']=='9993929488@t'):
            return "SUCCESS"
        else:
            return "Password is not correct"
    else:
        return "Some parameters are missing"
@app.route('/firebase-messaging-sw.js', methods=['GET'])
def sw():
    return app.send_static_file('firebase-messaging-sw.js')
@app.route("/getStat",methods=["GET"])
def getStats():
    return render_template("stats.html",totalRequests=getTotalRequests(),totalUsers=getUsers(),logouts=getLogouts(),failedAttempts=getFailedAttempts())
@app.route("/",methods = ["GET"])
def apires():
    if ('username' in request.args and 'password' in request.args):
        if (request.args['username'] == "123" and request.args['password'] == "123"):
            response = main("11156823968", "tushar#123")
        elif ('lnctu' in request.args):
            response = main(request.args['username'], request.args['password'],True)
        else:
            response = main(request.args['username'], request.args['password'])
        if (response == "error"):
            return "YOUR ID OR PASSWORD IS NOT CORRECT"
        else:
            apires = {
                "Name": response[0],
                "Total Lectures": response[1],
                "Present ": response[2],
                "Percentage": response[3],
                "Branch": response[4],
                "College": response[5],
                "Semester": response[6],
                "LecturesNeeded": response[7],
                'DaysNeeded': response[8]
            }
            return jsonify(apires)

    else:
        return render_template("index.html")
@app.route('/flutter_service_worker.js')
def w():
    return app.send_static_file('flutter_service_worker.js')
@app.route('/assets/<path:path>')
def static_proxy(path):
    return app.send_static_file('assets/' + path)
@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')
@app.route("/subjectwise",methods=["GET"])
def subject():
    if ('username' in request.args and "password" in request.args):
        if (request.args['username'] == "123" and request.args['password'] == "123"):
            response = subjectWise("11156823968", "tushar#123")
        elif ('lnctu' in request.args):
            response = subjectWise(request.args['username'], request.args['password'], True)
        else:
            response = subjectWise(request.args['username'], request.args['password'])
        if response == "error":
            return "YOUR ID OR PASSWORD IS NOT CORRECT"
        else:
            return jsonify(response)
    else:
        return "Some parameters are missing"
@app.route("/registerToken",methods=['POST'])
def registerToken():
    session.permanent = True
    session['token'] = request.json['token']
    firebase.database().child(session['username']).update({
        'token':request.json['token']
    })
    return request.json
@app.route('/dateWise')
def datewise():
    if ('username' in request.args and "password" in request.args):
        if (request.args['username'] == "123" and request.args['password'] == "123"):
            response = dateWise("11156823968", "tushar#123")
        elif ('lnctu' in request.args):
            response =dateWise(request.args['username'], request.args['password'],True)
        else:
            response = dateWise(request.args['username'], request.args['password'])

        if response == "error":
            return "YOUR ID OR PASSWORD IS NOT CORRECT"
        else:
            return jsonify(response)
    else:
        return "Some parameters are missing"

@app.route("/notify")
def notify():
    if('password' in request.args):
        if(request.args['password']=='9993929488@t'):
            getAttendance()
            return 'success'
        else:
            return 'you are not authorized'
    else:
        return 'Some parameters are missing'
if __name__ == "__main__":
    app.run()