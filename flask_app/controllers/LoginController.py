from flask_app import db

from flask import redirect,session,request,url_for,render_template,flash,jsonify


def index():
        if 'Email' in session:
                return redirect(url_for("predictions.index"))
        else:
                if request.method=='POST':
                        email = request.form['email_address']
                        password = request.form['password']

                        if email == "admin@gmail.com" and password == "admin123":
                                session['Email'] = email
                                session['Name'] = "admin"
                                return redirect(url_for("dashboard.index"))

                        else:
                                flash("Invalid Credentials",'Danger')
                                return redirect(url_for("login.index"))
                else:
                        return render_template('login.html')

def logout_account():
        if 'Email' in session:
                session.clear()
                return redirect(url_for("login.index"))

        else:
                return redirect(url_for("login.index"))