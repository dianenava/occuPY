
#from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

from flask import render_template, request
from flaskexample import app




# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.

# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.


user = 'diane' #add your Postgres username here      
host = 'localhost'
#dbname = 'activityperroom'
dbname = 'STARS'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

#a1 = request.arg.get(timeinterval)

@app.route('/')

#this is just the home page
@app.route('/input')
def index():
    return render_template("input.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )
@app.route('/input')
def activity_in():
    return render_template("input.html")

@app.route('/output')
def activity_out():
    return render_template("output.html")

@app.route('/reservationform')
def reservenow():
    return render_template("reservationform.html")
#@app.route("/test" , methods=['GET', 'POST'])
##   select = request.form.get('timeinterval')
  #  return(str(select)) # just to see what select is


@app.route('/output', methods=['GET', 'POST'])
#function that looks into the sequel server and returns the activity
def get_activity_machine():
    a1 = request.arg.get(timeinterval)
    
    #patient = request.args.get('birth_month')
    
    sql_query = """                                                                       
                SELECT * FROM testingtable;          
                """
    #query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
    
    #read a pandas tablle, convert into pandas
    query_results = pd.read_sql_query(sql_query,con)
    
    #query_results=pd.read_sql_query(query,con)
    
    activity = []   
    #births = []
    bins = []
    machines = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
    #x is column, a1 is row, we now have a1, 
    act1 = query_results.iloc[a1]['m1']
    
    
    for x in machines:
        activity = query_results.iloc[a1][x]
        #for example query_results.iloc[time=10]['machine1'] and call it activity
        if activity == 1:
            response = "OCCUPIED!!!"
        else:
            response = "Available"
        #based on this we have a response
        #store this value onto an activity array, with x as the index
        bins.append(response)
        
    m2activity, m3activity, m4activity, m5activity, m6activity = bins[1], bins[2], bins[3], bins[4], bins[5], bins[6]
    
    return render_template("output.html", act1 = act1, m2activity = m2activity, m3activity = m3activity, m4activity = m4activity, m5activity = m5activity, m6activity = m6ctivity)




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