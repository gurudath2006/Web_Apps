from flask import Flask, render_template,request, jsonify
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
db_username='postgres'
db_password='p@ssw0rd'
host='127.0.0.1'
port='5433'
database='AppointmentScheduler'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
# @app.route('/general-search')
# # this is how you define a function in Python
# def index():
#     # this is your index page
#     # connect to DB
#     cursor, connection = util.connect_to_db(username,password,host,port,database)
#     # execute SQL commands
#     record = util.run_and_fetch_sql(cursor, "SELECT * from customer;")
#     if record == -1:
#         # you can replace this part with a 404 page
#         print('Something is wrong with the SQL command')
#     else:
#         # this will return all column names of the select result table
#         # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
#         col_names = [desc[0] for desc in cursor.description]
#         # only use the first five rows
#         log = record[:5]
#         # log=[[1,2],[3,4]]
#     # disconnect from database
#     util.disconnect_from_db(connection,cursor)
#     # using render_template function, Flask will search
#     # the file named index.html under templates folder
#     return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/patient-login', methods=['GET'])
# this is how you define a function in Python
def patient_login():
    return render_template('patient_login.html')


@app.route('/patient-login', methods=['POST'])
def patient_login_validate():
    username = 'a.zimmer@gmail.com'
    password = 'test'
    
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "select * from public.\"Login\" Login where Login.\"Username\" ='"+username+"' and Login.\"Password\" = '"+password+"' and Login.\"RoleId\" = 2;")
    #record = util.run_and_fetch_sql(cursor, "select * from public.\"Login\";")
    # if len(record) <= 0 or record == -1:
    #     error='Incorrect login details provided. Please retry.'
    #     location=''
    # else:
    #     error = "select * from public.\"Login\" Login where Login.\"Username\" ='"+username+"' and Login.\"Password\" = '"+password+"' and Login.\"RoleId\" = 2;"
    #     location='general_search.html'
    #util.disconnect_from_db(connection=connection, cursor=cursor)
    #return jsonify(error=error,location=location)

if __name__ == '__main__':
	# set debug mode
    #app.debug = True
    # your local machine ip
    #ip = '127.0.0.1'
    #app.run(host=ip)
    patient_login_validate()

