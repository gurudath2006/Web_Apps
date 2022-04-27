Appointment Scheduler : 

Abstract:
Booking an appointment can be done in several ways like through phone call, in-person, e-mail, 
however the easiest and most convenient way of scheduling an appointment is online booking. It is user 
friendly as it does not require assistance from a third party and can be done at any given time of the 
day. There are numerous fields where an online appointment booking system can be of great help. 
Hospitals and clinics are the most significant beneficiaries as online appointment schedulers allow 
doctors to review their schedules at any given time and save time of the patients waiting on the phone 
calls during business hours to book an appointment. Patients or their family members can search for the 
providers close to their location and book an appointment with the doctor and get the right care based 
on the need. In addition to booking an appointment online, application can send a calendar invite to the 
patient after the booking is confirmed and send reminders to patient to notify about the appointment to 
ensure the patient does not miss the appointment.

Motivation:
Most of the health care providers require patients to phone their help desk to book an appointment and 
a lot of times phones are busy, patient must wait for a long time on the phone. Another limitation with 
the help desk booking is that the patient must call during business hours. In addition to that, they do not 
send timely reminders to the patients about their appointments and sometimes patients end up missing 
the appointment and paying the penalty fees. Considering this, we want to develop a website which can 
allow a patient to search for the providers near their location and choose the provider of right category 
based on their need and notify the patient about the appointment 72-hour, 24-hour, and 1-hour prior to 
the appointment. We also want to include video calls and audio call appointments which will help the 
elderly patients and patients who cannot take a trip to the hospitals and clinics 

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```
