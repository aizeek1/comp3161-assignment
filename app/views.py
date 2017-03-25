"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required


###
# Routing for your application.
###

@app.route('/home')

def home():
    """Render website's home page."""
    return render_template('home.html')
    
    
@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")
    
@app.route('/logout')
def logout():
    flash('You were logged out')
    return redirect(url_for('login'))
    
@app.route('/patient_disease/', methods=["GET", "POST"])
def patient_disease():
    return render_template("PatientsWithSelectedDisease.html")
    
@app.route('/patient_allergies/', methods=["GET", "POST"])
def patient_allergies():
    return render_template("PatientsAllergies.html")
    
@app.route('/allergic_medication/', methods=["GET", "POST"])
def allergic_medication():
    return render_template("MostAllergicMedication.html")
    
@app.route('/patient_results/', methods=["GET", "POST"])
def patient_results():
    return render_template("PatientsResults.html")
    
@app.route('/nurse_medication/', methods=["GET", "POST"])
def nurse_medication():
    return render_template("NursesAdministeredMedication.html")
    
@app.route('/interns/', methods=["GET", "POST"])
def interns():
    return render_template("InternsTreatedMostPatients.html")
    
@app.route('/register/', methods=["GET", "POST"])
def register():
    return render_template("register.html")
    
@app.route('/medical_info/', methods=["GET", "POST"])
def medical_info():
    return render_template("medical_info.html")
    
@app.route('/medical_record/', methods=["GET", "POST"])
def medical_record():
    return render_template("medical_record_system.html")
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
