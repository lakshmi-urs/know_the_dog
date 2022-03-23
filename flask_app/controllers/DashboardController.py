import hashlib
# For Hashing Password

from flask_app import db

# from ..models.pypies import Pypies 
# from ..models.users import User
from flask import redirect,session,request,url_for,render_template,flash,jsonify


def index():
        if 'Email' in session:
                return render_template('index.html')
        else:
                return redirect(url_for("predictions.index"))

def dashboard_page():
        if 'Email' in session:
                return render_template('index.html')
        else:
                return redirect(url_for("predictions.index"))
#     if 'Email' in session:

#         if request.method == "POST":
#             name = request.form['name']
#             filling = request.form['filling']
#             crust= request.form['crust']
#             email = session['Email']
            
#             info = {
#                 'name': name,
#                 'filling': filling,
#                 'crust': crust,
#                 'user_email': email
#             }
#             pypie = Pypies(info)           
#             db.session.add(pypie)
#             db.session.commit()
#             #  PyPie is added
#             return redirect(url_for("dashboard.index"))
#         else:

#             # Get all the Pypies of the user
#             pypie = []
#             result = Pypies.query.filter_by(user_email = session['Email']).all()
#             for prod in result:
#                 pypie.append(prod)
#             return render_template("dashboard.html",pypie = pypie)

#     else:
#         return redirect(url_for("users.index"))



# def delete():
#     if 'Email' in session:
#         if request.method == "POST":
#             item_id = request.form['item_id']
#             db.session.query(Pypies).filter_by(id=int(item_id)).delete()
#             db.session.commit()
#             flash("Item successfully deleted","success")
#             return redirect(url_for('dashboard.index'))
#         else:
#             flash("Access denied","danger")
#             return redirect(url_for("users.index"))

#     else:
#         flash("Access denied","danger")
#         return redirect(url_for("users.index"))
       






# @app.route('/confirm-email<token>',methods=["GET","POST"])
# def confirmEmail(token):
#     if 'Email' in session:
#         return redirect(url_for("prediction"))
#     else: 
#             try:
#                 # Email is stored in the token
#                 email = token_key.loads(token, salt='email-confirmation', max_age=3600)

#                 # # Confirm Email
#                 result = user_temp.query.filter_by(email = email).first()
                
#                 if result.confirmation == 1: 
#                     form = SignUpForm()
#                     leagues = []
#                     results = league.query.all() 
#                     for leag in results:
#                         leagues.append(leag)
#                     countriesData = countries.query.all() 
            

#                     country = []


#                     for coun in countriesData:
#                         country.append(coun)

                   

#                     return render_template("landing_page.html",form=form,leagues=leagues,country=country,status_code=400)

#                 else:

#                     form = SignUpForm()
#                     leagues = []
#                     results = league.query.all() 
#                     for leag in results:
#                         leagues.append(leag)
#                     countriesData = countries.query.all() 
            
#                     country = []
#                     for coun in countriesData:
#                         country.append(coun)
                        
#                     return render_template("signup.html",email=email,leagues=leagues,country=country,status_code = 204,token=token,form=form)
            
                    
#             except SignatureExpired:
#                 return jsonify({
#                         "status": 400,
#                         "message": "Your link is expired"
#                     })

