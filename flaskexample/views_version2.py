#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:28:22 2018

@author: diane


"""

from flask import render_template
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
@app.route('/db')
def activity():
    sql_query = """                                                                       
                SELECT * FROM birth_data_table WHERE delivery_method='Cesarean';          
                """
    query_results = pd.read_sql_query(sql_query,con)
    births = ""
    
    machines = [machine1, machine2, machine3, machine4, machine5, machine6]
    for item in machines:
        births += query_results.iloc[i][item]
        births += "<br>"
    return activity

#did this save?


@app.route("/upload", methods=["POST"])
def upload():
    #target = os.path.join(APP_ROOT, 'images/')
    target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        #change this to filename
        destination = "/".join([target, "rooms.png"])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("new.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
    
    

        
   # return activity
   
   
   @app.route('/reserve', methods=['POST'])
def reserve():
    return render_template("reservationform.html")

    projectpath = request.form['projectFilepath']
    # your code
    # return a response


def contact():
    if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            pass # do something
        elif request.form['submit'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
#post is to send data from the client to the server

    
@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text