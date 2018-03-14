# Infrastructure test page.
import os
import sys
from flask import Flask
from flask import Markup
from flask import render_template
from flask import request
# from flask_sqlalchemy import SQLAlchemy
from dbhelper import DBHelper

app = Flask(__name__)
db = DBHelper()

@app.route("/")
def index():
    # data = db.select("SELECT * FROM users ORDER BY id DESC")
    # print(data)
    return render_template('index.html')


@app.route("/finduser", methods=["GET"])
def finduser():
    print("[*] Find user")
    print(request)
    sql = "select * from users where user = '{0}'".format(request.args.get("user"))
    print(sql)
    data = db.select(sql)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
