from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('firstapp.html', message="Hello")

@app.route("/oshimen")
def oshimen():
    return render_template("oshimen.html")

@app.route("/oshimen/oshiinfo",methods=['POST','GET'])
def oshimen_return():
    if request.method=='POST':
        name=request.form["name"]
        return render_template("oshiinfo.html",name=name)

@app.route("/hello")
def hello():
    val=request.args.get("msg", "Not defined")
    return "Hello World" + val

if __name__=="__main__":
    app.run()