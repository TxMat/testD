from flask import Flask, send_from_directory, request, render_template, Markup
from src.model.model import Model
from src.model.user_exception import *
from datetime import date, datetime

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
    return render_template("PageAccueil.html")

@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('PageConnexion.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = None
        try:
            user = model.load_user(username, password)
        except UserNotFound:
            error_feedback = 'L\'adresse meil est inconnue'
            return render_template('PageConnexion.html', error_feedback=error_feedback)
        except IncorrectPassword:
            print("incorrect pass")
            error_feedback = 'Mot de passe incorrect'
            return render_template('PageConnexion.html', error_feedback=error_feedback)

        return render_template('PageAccueilLogged.html', user=user)
        
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('PageInscription.html')
    else:
        errors_feedbacks = []
        user = None
        try:
            name = request.form['name']
            lastname = request.form['lastname']
            mail = request.form['mail']
            password = request.form['password']
            confirm = request.form['confirm']
            birthday_str = request.form['birthday']
            birthday = datetime.fromisoformat(birthday_str)
            
        except (KeyError, ValueError):
            errors_feedbacks = "Erreur requête"
        if errors_feedbacks == []:
            try:
                user = model.create_user(name, lastname, mail, password, birthday)
            except UserCreationException as e:
                for feedback in e.feedback:
                   
                   errors_feedbacks.append(feedback.value.replace("\n", "<br>"))
        if errors_feedbacks != []:
            print(errors_feedbacks)
            return render_template('PageInscription.html', errors_feedbacks=errors_feedbacks)
        else:
            return render_template('PageAccueilLogged.html', user=user)