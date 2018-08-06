from flask import Flask, render_template, request
import bs4
import lxml
from bs4 import BeautifulSoup
import re
import requests
# test
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('firstapp.html', message="Hello")

@app.route("/oshimen_search")
def oshimen():
    return render_template("oshimen.html")

@app.route("/oshiinfo",methods=['POST','GET'])
def oshimen_return():
    if request.method=='POST':
        try:
            name=request.form["name"]
            html=requests.get("https://48pedia.org/" + str(name))
            soup=BeautifulSoup(html.text,'lxml')
            url=soup.find('a',class_='image').get('href')
            html=requests.get('https://48pedia.org' + str(url))
            soup=BeautifulSoup(html.text,'lxml')
            img_link=soup.find('a',href=re.compile("^/images/")).get('href')
            return render_template("oshiinfo.html",name=name,link=img_link)
        except:
            return render_template("oshiinfo.html",message='メンバーが見つかりません')


if __name__=="__main__":
    app.run(debug=True)