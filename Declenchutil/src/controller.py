from flask import Flask, send_from_directory, request, render_template
from src.model.model import Model
from src.model.user_exception import *
from datetime import date

model = Model()
app = Flask(__name__, template_folder='../html')
def run():
    
    try:
        model.create_user('Loic', 'PIERNAS', 'lpiernas.pers@gmail.com', 'StrongPwd123!!', date(day=8, month=3, year=2002))
    except UserAlreadyExists:
        pass
    app.run(debug=True)

@app.route("/css/<path:path>")
def css(path):
    return send_from_directory('../css', path)

@app.route("/img/<path:path>")
def img(path):
    return send_from_directory('../img', path)

@app.route('/')
def index():
    return render_template("PageAcceuil.html")

@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('PageConnexion.html')
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            user = model.load_user(username, password)
        except UserNotFound:
            error_feedback = 'L\'adresse meil est inconnue'
            return render_template('PageConnexion.html', error_feedback=error_feedback)
        except IncorrectPassword:
            print("incorrect pass")
            error_feedback = 'Mot de passe incorrect'
            return render_template('PageConnexion.html', error_feedback=error_feedback)
        

        return render_template('PageAcceuilLogged.html')
        
