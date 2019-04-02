from flask import Flask,render_template,request,redirect,jsonify
from main import main
# We are importing Cors to enable cross origin requests(cors)
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/api",methods = ["GET","POST","PUT"])
def api():

    if('App-id' in request.headers and 'username' in request.args and "password" in request.args):
        if request.headers['App-Id'] == '999T39U29S488':
            response = main(request.args['username'],request.args['password'])
            if response == "error":
                return "YOUR ID OR PASSWORD IS NOT CORRECT \n However you got the right Api key"
            else:
                apires = {
                    "Name":response[1],
                    "Image Url":response[0],
                    "Total Lectures" :response[2],
                    "Present ":response[3]
                }
                return jsonify(apires)
        else:
            return "API key is not correct"

    else:
        return "Some parameters are missing"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")
@app.route("/attendance",methods = ["POST","GET"])
def attendance():
    if request.method =="POST":
        list = main(request.form['username'],request.form['password'])
        if list == "error":
            return render_template("error.html")
        return render_template("attendance.html",img=list[0],name=list[1],total=list[2],present=list[3])
    elif request.method =="GET":
        return redirect("/")

if __name__ == "__main__":
    app.run()
