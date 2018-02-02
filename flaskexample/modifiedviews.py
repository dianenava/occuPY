
#from flaskexample import app
#from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import pandas as pd
#import psycopg2

from flask import render_template, request
from flaskexample import app



# import things
from flask_table import Table, Col

# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.

# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.


#user = 'diane' #add your Postgres username here      
#host = 'localhost'
#dbname = 'activityperroom'
#dbname = 'STARS'
#db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
#con = None
#con = psycopg2.connect(database = dbname, user = user)

#a1 = request.arg.get(timeinterval)

@app.route('/')

#this is just the home page
@app.route('/index')
def index():
    return render_template("open.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )
    
@app.route('/modifiedinput')
def activity_in():
    return render_template("modifiedinput.html")

@app.route('/parking')
def activity_parking():
    return render_template("parking.html")

@app.route('/output')
def activity_out():
    return render_template("output.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/out_machine1')
def out_machine1():
    return render_template("out_machine1.html")

@app.route('/out_machine2')
def out_machine2():
    return render_template("out_machine2.html")

@app.route('/out_machine3')
def out_machine3():
    return render_template("out_machine3.html")

@app.route('/out_machine4')
def out_machine4():
    return render_template("out_machine4.html")

@app.route('/out_machine5')
def out_machine5():
    return render_template("out_machine5.html")

@app.route('/out_machine6')
def out_machine6():
    return render_template("out_machine6.html")

@app.route('/outparking8')
def outparking8():
    return render_template("outparking8.html")

@app.route('/outparking2')
def outparking2():
    return render_template("outparking2.html")

@app.route('/output', methods=['GET', 'POST'])
#function that looks into the sequel server and returns the activity
def get_activity_machine():
    a1 = request.arg.get(timeinterval)
    
    #patient = request.args.get('birth_month')
    

    #query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
    
    #read a pandas tablle, convert into pandas
    #NO query_results = pd.read_sql_query(sql_query,con)
    query_results = pd.read_csv('/static/true_values_transposed.csv')
    
    
    
    #query_results=pd.read_sql_query(query,con)
    
    activity = []   
    #births = []
    bins = []
    machines = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
    #x is column, a1 is row, we now have a1, 
    #act1 = query_results.iloc[a1]['m1']
    
    
    for x in machines:
        activity = query_results.iloc[a1][x]
        #for example query_results.iloc[time=10]['machine1'] and call it activity
        print(x)
        print(activity)
        if activity == 1:
            response = "OCCUPIED!!!"
        else:
            response = "Available"
        print(response)
        #based on this we have a response
        #store this value onto an activity array, with x as the index
        bins.append(response)
        
    m1activity, m2activity, m3activity, m4activity, m5activity, m6activity = bins[0], bins[1], bins[2], bins[3], bins[4], bins[5]

    return render_template("output.html", m1activity=m1activity, m2activity = m2activity, m3activity = m3activity, m4activity = m4activity, m5activity = m5activity, m6activity = m6ctivity)
    print(bins)


#@app.route('/output', methods=['GET', 'POST'])
#function that looks into the sequel server and returns the activity
#def get_activity_machine():
 #   a1 = request.arg.get(machine)
    
  #  if a1 == 1:
   #     return render_template("output.html")
    #elif a1 ==2:
     #   return render_template("modifiedoutput2.html")
    #else:
     #   return render_template("modifiedinput.html")

    
  






def cesareans_output():
  #pull 'birth_month' from input field and store it
  
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
  
  print(query)
  
  print(query_results)
  
  for i in range(0,query_results.shape[0]):
      births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
      the_result = ''
  return render_template("output.html", births = births, the_result = the_result)


















@app.route('/index', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        select = request.form.get('timeinterval')
        return(str(select))
    else:
        # You probably don't have args at this route with GET
        # method, but if you do, you can access them like so:
        yourarg = flask.request.args.get('argname')
        your_register_template_rendering(yourarg)







@app.route('/new')
def assign_time():
    #if the input of the user in the html page for the timebox is A, set the i values to a certain thing
    #get the timeinterval value
    a1 = request.arg.get(timeinterval)
    return a1
    #use this a1 to be the index for the sql distribution of activity
    








if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.run()