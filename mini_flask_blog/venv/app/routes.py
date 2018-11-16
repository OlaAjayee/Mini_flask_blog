from flask import render_template, flash, redirect, request, url_for, session, escape
# from flask_login import logout_user
from app import app
from app.forms import LoginForm
from app.forms import SignupForm
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open('db.txt', 'r') as file:
            for line in file:  
                db_username, password_hash = line.split('|')
                password_hash = password_hash.strip('\n')
                if db_username == username:
                    if check_password_hash(password_hash, password):
                        flash('You were successfully logged in')
                        return redirect(url_for('index'))
                        
                
        login_error = 'Invalid username or password. Please try again!'
        return render_template('login.html', error=login_error)
    elif request.method == 'GET':
        return render_template('login.html', title='Sign In', form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up', form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    with open('db.txt', 'a') as file:
        password_hash = generate_password_hash(password)

        db_record = '|'.join([username, password_hash])
        file.write(db_record + '\n')
        flash(f'Your username is  "{username}" and password is "{password}"')
        return redirect(url_for('login'))\

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ola'}
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
    posts = [
        { 
            'author': {'username': 'John'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

    # if 'username' in session:
    #     return 'Logged ub as %s' % escape(session['username'])
    # return 'You are not logged in'



