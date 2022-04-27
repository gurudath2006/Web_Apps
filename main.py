from flask import Flask, render_template,request, jsonify
import util,json
from datetime import datetime
from datetime import timedelta

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

@app.route('/', methods=['GET'])
# this is how you define a function in Python
def index():
    return render_template('index.html')

# @app.route('/<patient_id>', methods=['GET'])
# # this is how you define a function in Python
# def index(patient_id):
#     cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
#     patient = util.run_and_fetch_sql_objects(cursor, "SELECT \"PatientId\", \"FirstName\", \"LastName\", \"Email\" FROM public.\"Patient\" where \"Patient\".\"PatientId\" = " + patient_id + ";")
#     patient_json = json.loads(patient)
    
#     util.disconnect_from_db(connection=connection, cursor=cursor)
#     return render_template('index.html',patient_json)

@app.route('/patient-login', methods=['GET'])
# this is how you define a function in Python
def patient_login():
    return render_template('patient_login.html')


@app.route('/patient-login', methods=['POST'])
def patient_login_validate():
    username = request.form['username']
    password = request.form['password']
    
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "select * from public.\"Login\" Login where Login.\"Username\" ='"+username+"' and Login.\"Password\" = '"+password+"' and Login.\"RoleId\" = 2;")
    patient_id = 0
    if len(record) <= 0 or record == -1:
        error='Incorrect login details provided. Please retry.'
        location=''
    else:
        patient = util.run_and_fetch_sql_objects(cursor, "SELECT \"PatientId\", \"FirstName\", \"LastName\", \"Email\" FROM public.\"Patient\" where lower(\"Patient\".\"Email\") = lower('" + username + "');")
        patient_json = json.loads(patient)
        error = ''
        location = 'general-search/' + str(patient_json[0]["PatientId"])
    util.disconnect_from_db(connection=connection, cursor=cursor)
    return jsonify(error=error,location=location)

@app.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    patient_id = request.form['patient_id']
    provider_id = request.form['provider_id']
    booking_date = request.form['booking_date']
    
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    util.run_sql(cursor, "INSERT INTO public.\"PatientBooking\"(\"PatientId\", \"ProviderId\", \"BookingDate\") VALUES ("+ patient_id +","+ provider_id +",'" + booking_date + "');")
    connection.commit()

    events_json = get_provider_availability(provider_id)
    patient_bookings_str = get_patient_bookings(patient_id,provider_id)    
    util.disconnect_from_db(connection=connection, cursor=cursor)
    return jsonify(events = events_json, patient_bookings_str = patient_bookings_str)

@app.route('/cancel-booking', methods=['POST'])
def cancel_booking():
    patient_id = request.form['patient_id']
    provider_id = request.form['provider_id']
    booking_date = request.form['booking_date']
    
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    util.run_sql(cursor, "DELETE FROM public.\"PatientBooking\"	WHERE public.\"PatientBooking\".\"ProviderId\" = " + provider_id + " and public.\"PatientBooking\".\"PatientId\" = " + patient_id + " and public.\"PatientBooking\".\"BookingDate\" = '" + booking_date + "';")
    connection.commit()

    events_json = get_provider_availability(provider_id)
    patient_bookings_str = get_patient_bookings(patient_id,provider_id)    
    util.disconnect_from_db(connection=connection, cursor=cursor)
    return jsonify(events = events_json, patient_bookings_str = patient_bookings_str)


@app.route('/general-search/<patient_id>', methods=['GET'])
def general_search(patient_id=''):
    
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    service_category_list = util.run_and_fetch_sql_objects(cursor, "SELECT \"ServiceCategoryId\", \"ServiceCategoryName\" FROM public.\"ServiceCategory\";")
    provider_list = util.run_and_fetch_sql_objects(cursor, "SELECT \"FirstName\", \"LastName\", public.\"ServiceCategory\".\"ServiceCategoryId\", public.\"ServiceCategory\".\"ServiceCategoryName\", \"Address\", \"Email\", \"ProviderId\", \"Phone\", \"LocationId\" FROM public.\"Provider\" inner join public.\"ServiceCategory\" on public.\"Provider\".\"ServiceCategoryId\" = public.\"ServiceCategory\".\"ServiceCategoryId\";")
    patient_json = ''
    if(patient_id != ''):
        patient = util.run_and_fetch_sql_objects(cursor, "SELECT \"PatientId\", \"FirstName\", \"LastName\", \"Email\" FROM public.\"Patient\" where \"Patient\".\"PatientId\" = " + patient_id + ";")
        patient_json = json.loads(patient)
    service_category_json = json.loads(service_category_list)
    provider_json = json.loads(provider_list)
    
    util.disconnect_from_db(connection=connection, cursor=cursor)
    return render_template('General_Search.html',service_category_json=service_category_json,provider_list=provider_json, patient=patient_json)

@app.route('/book-appointment', methods=['GET'])
def book_appointment_error():
    return book_appointment('','')

@app.route('/provider-availability/<provider_id>', methods=['GET'])
def provider_availability(provider_id=''):
    events = get_provider_availability(provider_id)
    return jsonify(events=events)

def get_provider_availability(provider_id=''):
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    provider_availability = util.run_and_fetch_sql_objects(cursor, "SELECT \"ProviderAvailabilityId\", public.\"ProviderAvailability\".\"ProviderId\", CAST(public.\"ProviderAvailability\".\"AvailableDate\" AS text) FROM public.\"ProviderAvailability\" left outer join public.\"PatientBooking\" on public.\"PatientBooking\".\"ProviderId\" = public.\"ProviderAvailability\".\"ProviderId\" and public.\"PatientBooking\".\"BookingDate\" =  public.\"ProviderAvailability\".\"AvailableDate\" where public.\"PatientBooking\".\"BookingDate\" is null AND public.\"ProviderAvailability\".\"AvailableDate\" > CURRENT_DATE + INTERVAL '1 day' and public.\"ProviderAvailability\".\"ProviderId\" = " + provider_id +";")
    provider_availability_json = json.loads(provider_availability)    
    
    events = []
    for availability in provider_availability_json:
        available_date = datetime.fromisoformat(availability["AvailableDate"]) 
        start = available_date.strftime("%Y-%m-%dT%H:%M:%S")
        endDateTime = available_date + timedelta(hours=1)
        end = endDateTime.strftime("%Y-%m-%dT%H:%M:%S")
        event = {"start": start, "end": end, "display": "background"}
        events.append(event)
        
    util.disconnect_from_db(connection=connection, cursor=cursor)
    return events

def get_patient_bookings(patient_id='',provider_id=''):
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    patient_bookings = util.run_and_fetch_sql_objects(cursor, "SELECT \"PatientBookingId\", \"PatientId\", \"ProviderId\", CAST(public.\"PatientBooking\".\"BookingDate\" AS text)  \"BookingDate\" FROM public.\"PatientBooking\" where public.\"PatientBooking\".\"PatientId\" = "+ patient_id +" and public.\"PatientBooking\".\"ProviderId\" = "+ provider_id +" ;")
    patient_bookings_json = json.loads(patient_bookings)    
            
    util.disconnect_from_db(connection=connection, cursor=cursor)
    patient_bookings_str = ''
    index = 1
    if(len(patient_bookings_json)>0):
        for booking in patient_bookings_json:
            patient_bookings_str = patient_bookings_str + '<tr><th scope="row">'+ str(index) +'</th><td>'+ str(booking["BookingDate"]) +'</td><td><a id="model-cancel-booking-button" booking-date="'+ str(booking["BookingDate"]) +'" href="#!">X</a></td></tr>'
            index = index + 1
    return patient_bookings_str

@app.route('/book-appointment/<patient_id>/<provider_id>', methods=['GET'])
def book_appointment(patient_id='', provider_id=''):
    
    if(provider_id == '' or patient_id == '') :
        return render_template('Book_Appointment.html',error='Invalid page access')
    # # connect to DB
    cursor, connection = util.connect_to_db(db_username,db_password,host,port,database)
    # # execute SQL commands
    provider_detail = util.run_and_fetch_sql_objects(cursor, "SELECT \"FirstName\", \"LastName\", public.\"ServiceCategory\".\"ServiceCategoryId\", public.\"ServiceCategory\".\"ServiceCategoryName\", \"Address\", \"Email\", \"ProviderId\", \"Phone\", \"LocationId\" FROM public.\"Provider\" inner join public.\"ServiceCategory\" on public.\"ServiceCategory\".\"ServiceCategoryId\" = public.\"Provider\".\"ServiceCategoryId\" where public.\"Provider\".\"ProviderId\" = " + provider_id)
    patient = util.run_and_fetch_sql_objects(cursor, "SELECT \"PatientId\", \"FirstName\", \"LastName\", \"Email\" FROM public.\"Patient\" where \"Patient\".\"PatientId\" = " + patient_id + ";")
    provider_availability = util.run_and_fetch_sql_objects(cursor, "SELECT \"ProviderAvailabilityId\", \"ProviderId\", CAST(\"AvailableDate\" AS text) FROM public.\"ProviderAvailability\" where public.\"ProviderAvailability\".\"ProviderId\" = " + provider_id +";")
    provider_detail_json = json.loads(provider_detail)
    provider_availability_json = json.loads(provider_availability)    
    patient_json = json.loads(patient)   
    patient_bookings_str = get_patient_bookings(patient_id,provider_id)
    util.disconnect_from_db(connection=connection, cursor=cursor)
    initial_date = datetime.today().strftime('%Y-%m-%d')
    return render_template('Book_Appointment.html',patient_bookings_str = patient_bookings_str, patient=patient_json, provider=provider_detail_json[0],initial_date=initial_date, error='')


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

