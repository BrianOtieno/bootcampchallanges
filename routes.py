from flask import Flask, request, render_template, url_for, session, redirect
from models.models import db, User, Comments, Diary
from forms import RegistrationForm, LoginForm, PostCommentForm, DiaryForm, API_Resigration, Token
from werkzeug import generate_password_hash, check_password_hash
from wtforms.validators import Email, Length, InputRequired
import psycopg2

app = Flask(__name__, static_url_path='')

#upgrade to SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:\
5ure5t@re!@localhost/andelalevelup'

db.init_app(app)

app.secret_key = "bootcamp-key"


@app.route("/login", methods=["GET", "POST"])
def login():
    if 'email'in session:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = user.email
                session['firstname'] = user.firstname
                return redirect(url_for('homepage'))
            else:
                return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template('login.html', form=form)


@app.route("/homepage")
def homepage():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("homepage.html")

@app.route("/navigation")
def navigation():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("navigation.html")

@app.route("/comments")
def comments():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("getcomments.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit() == False:
            return render_template("register.html", form=form)
        else:
            newaccount = User(form.firstname.data, form.lastname.data, \
            form.phonenumber.data, form.email.data, form.password.data)
            db.session.add(newaccount)
            db.session.commit()

            session['email'] = newaccount.email
            session['firstname'] = newaccount.firstname
            return redirect(url_for('homepage'))

    elif request.method == "GET":
        return render_template("register.html", form=form)

@app.route("/diary", methods=['GET','POST'])
def diary():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = DiaryForm()

    if request.method =="POST":
        if form.validate() == False:
            return render_template("diary.html", form=form)
        else:
            newdiary = Diary(form.event.data, form.eventname.data)
            db.session.add(newdiary)
            db.session.commit()

            return redirect(url_for('homepage'))

    elif request.method == "GET":
        return render_template('diary.html', form=form)

@app.route("/postcomment", methods=['GET','POST'])
def postcomment():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = PostCommentForm()

    if request.method =="POST":
        if form.validate() == False:
            return render_template("postcomments.html", form=form)
        else:
            newpost = Comments(form.title.data,form.comment.data)
            db.session.add(newpost)
            db.session.commit()

            return redirect(url_for('comments'))

    elif request.method == "GET":
        return render_template('postcomments.html', form=form)

@app.route("/allcomments")
def allcomments():
    return render_template("allcomments.html")

@app.route("/api/registration", methods=['GET'])
def api_registration():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = API_Resigration()
    return render_template('apiregistration.html', form=form)

@app.route("/account")
def account():
    pass

@app.route("/token", methods=['GET'])
def token():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = Token()
    return render_template('token.html', form=form)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8081)
