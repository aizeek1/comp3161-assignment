"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required


# prepare a cursor object using cursor() method
cursor = db.cursor()

empnum=''
patnum=8

###
# Routing for your application.
###



@app.route("/", methods=["GET", "POST"])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        employeeid = request.form['empID']
        password = request.form['password']
        pos=getPosition(employeeid)
        session['position']=pos
        if getUserInfo(employeeid,password):
             session['logged_in'] = True
             session['empId']= employeeid
             
             flash('You are logged in')
             return redirect(url_for('home'))
        else:
            flash('Incorrect password')
    return render_template("login.html")
    
@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login'))
    
@app.route('/home')

def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/patient_disease/', methods=["GET", "POST"])
def patient_disease():
    if request.method == 'POST':
        diagnosis=request.form['diag']
        datefr=request.form['datefr']
        dateto=request.form['dateto']
        dis=getDiseases(diagnosis,datefr,dateto)
    return render_template("PatientsWithSelectedDisease.html")
    
@app.route('/patient_allergies/', methods=["GET", "POST"])
def patient_allergies():
    return render_template("PatientsAllergies.html")
    
@app.route('/allergic_medication/', methods=["GET", "POST"])
def allergic_medication():
    return render_template("MostAllergicMedication.html")
    
@app.route('/patient_results/', methods=["GET", "POST"])
def patient_results():
    if request.method == 'POST':
       
        patientid=request.form['patientid']
        results=getPatientResults(patientid)
    return render_template("PatientsResults.html")
    
@app.route('/nurse_medication/', methods=["GET", "POST"])
def nurse_medication():
    return render_template("NursesAdministeredMedication.html")
    
@app.route('/interns/', methods=["GET", "POST"])
def interns():
    return render_template("InternsTreatedMostPatients.html")
    
@app.route('/register/', methods=["GET", "POST"])
def register():
    
    if request.method == 'POST':
        
        fname=request.form['fname']
        mname=request.form['mname']
        lname=request.form['lname']
        dob=request.form['dob']
        gender=request.form['gender']
        street=request.form['street']
        city=request.form['city']
        phone=request.form['phone']
        global patnum
        patnum += 1
        #patnum= cursor.execute('SELECT MAX(patientID) FROM patients')
        
        pID= 'P-0000000' + str(patnum)
        
        #execute sql commands
        cursor.execute("INSERT INTO patients VALUES ('{}','{}','{}','{}','{}','{}')".format(pID,lname,fname,mname,gender,dob))
        cursor.execute("INSERT INTO patient_phoneno VALUES ('{}','{}')".format(pID,phone))
        cursor.execute("INSERT INTO patient_address VALUES ('{}','{}','{}')".format(pID,city,street))
        
        #commit changes to the database
        db.commit()
        
        #in case there is any error
        #db.rollback()
    return render_template("register.html")
    
@app.route('/medical_info/', methods=["GET", "POST"])
def medical_info():
    if request.method == 'POST':
        empID=request.form['empID']
        patientID=request.form['patientID']
        fname=request.form['fname']
        lname=request.form['lname']
        vitals=request.form['vitals']
        diagnosis=request.form['diagnosis']
        dcode=request.form['dcode']
        dor=request.form['dor']
        treatmentid=request.form['treatmentid']
        treatmenttype=request.form['treatmenttype']
        dateoftreatment=request.form['dateoftreatment']
        medication=request.form['medication']
        redirect(url_for('home'))
    return render_template("medical_info.html")

@app.route('/results/', methods=["GET", "POST"])
def results():
    return render_template("results.html")
    
@app.route('/medical_record/', methods=["GET", "POST"])
def medical_record():
    return render_template("medical_record_system.html")
    

def getPosition(employeeid):
    pos="SELECT position FROM employee WHERE employeeID = '{}'".format(employeeid) 
    cursor.execute(pos)
    position=cursor.fetchall()
    
    if position == 'Secretary':
        print position
        return position
    elif position == 'Doctor' or position == 'Nurse':
        print position
        return position
        
def getDiseases(diagnosis,datefr,dateto):
    sql="SELECT patient_fname,patient_mname,patient_lname from patients WHERE patientID in( SELECT patientID from record WHERE diagnosisID = '{}')".format(diagnosis)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
    
def getUserInfo(employeeid,password):
    sql = "SELECT employeeID,password FROM employee WHERE employeeID = '{}'".format(employeeid) 
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
 
    ## cursor.execute("select employeeID,password from employee where employeeID = %s " % 'employeeid')
    ## results = cursor.fetchone()
    ## for row in results:
        global empnum
        empnum=row[0]
        pwd=row[1]
        # print "[SQL-2]: {}".format(row)
    if employeeid == str(empnum) and password==pwd:
        return True
        
def getPatientResults(patientid):
    sql= "select * from patient where patientID = %s " % "patientid"
    cursor.execute(sql)
    results = cursor.fetchone()
    return results

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
