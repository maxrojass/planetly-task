from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tippytrip@localhost/planetly-task'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
@app.route('/')
def home():
    return '<h5>Please click below to access the API</h5><a href="/menu"><button> Click here </button></a>'


@app.route("/menu")
def menu():
    return render_template("index.html")


@app.route("/selection", methods=['POST'])
def selection():
    select = request.form['choice']
    if select == '1':
        select = '1'
        return render_template("add.html")
    elif select == '2':
        select = '2'
        return render_template("update.html")
    else:
        select = '3'
        return render_template("topn.html")
    
    
@app.route("/add", methods=['POST'])
def add():
    dt = request.form["dt"]
    city = request.form["city"]
    country = request.form["country"]
    averagetemperature = request.form["averagetemperature"]
    averagetemperatureuncertainty = request.form["averagetemperatureuncertainty"]
    latitude = request.form["latitude"]
    longitude = request.form["longitude"]
    values = "'"+dt+"'" +', '+ "'"+str(averagetemperature)+"'"+', '+"'" +str(averagetemperatureuncertainty) +"'" +', '+"'"+ city+"'"+ ', '+"'"+country+"'"+ ', '+"'"+str(latitude)+"'"+ ', '+"'"+str(longitude)+"'"
    insert = "INSERT INTO Global_Land_Temperatures_By_City (dt, averagetemperature,averagetemperatureuncertainty, city, country, latitude, longitude) VALUES ("+values+")"
    result = db.engine.execute(insert)
    return render_template("done.html")

@app.route("/update", methods=['POST'])
def update():
    select = request.form['option']
    if select == '1':
        select = '1'
        return render_template("updateavg.html")
    else:
        select = '2'
        return render_template("updateunc.html")    

@app.route("/updateavg", methods=['POST'])
def updateavg():
    dt = request.form["dt"]
    city = request.form["city"]
    country = request.form["country"]
    averagetemperature = request.form["averagetemperature"]
    update_avg_temp = "UPDATE Global_Land_Temperatures_By_City SET averagetemperature = "+averagetemperature+" where dt = '"+dt+"' and city = '"+city+"'"
    result = db.engine.execute(update_avg_temp)
    return render_template("done.html")

@app.route("/updateunc", methods=['POST'])
def updateunc():
    dt = request.form['dt']
    city = request.form['city']
    country = request.form["country"]
    averagetemperatureuncertainty = request.form["averagetemperatureuncertainty"]
    update_avg_temp_uncer = "UPDATE Global_Land_Temperatures_By_City SET averagetemperatureuncertainty = "+averagetemperatureuncertainty+" where dt = '"+dt+"' and city = '"+city+"'"
    result = db.engine.execute(update_avg_temp_uncer)
    return render_template("done.html")

@app.route("/topn", methods =['POST', "GET"])
def topn():
    db_string = "postgresql://postgres:tippytrip@localhost/planetly-task"
    db = create_engine(db_string)
    dt1 = request.form['dt1']
    dt2 = request.form['dt2']
    N = request.form['n']
    query = "SELECT * FROM Global_Land_Temperatures_By_City WHERE dt between '"+ dt1 +"' and '"+dt2+"' and averagetemperature IS NOT NULL ORDER BY averagetemperature DESC LIMIT "+ N
    df = pd.read_sql_query(query,con=db)
    return render_template('table.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

    
if __name__ == '__main__':
    app.debug = True
    app.run()