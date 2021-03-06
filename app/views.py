import db_manager
from geoip import geolite2,IPInfo
from flask import Flask, render_template, redirect, jsonify, url_for, request,session,escape
from app import app, models, db
from .forms import AddListingForm

#idafsdalfasdfl;akjdsflj
app.secret_key = 'hubbahubba'
@app.route('/')
@app.route('/index')
def index():
    error = None
    for key in session:
        print(key)
    if 'username' in session:
        # here we would want to verify that the user is in the databases
        print('DO I GET HERE')
        username = session['username']
        session.pop('username',None)
        return redirect(url_for('landing'))
    print('CHANGE')
    return redirect(url_for('login'))
##################--- AJAX TESTING SCHEME ---############  
@app.route('/ajax')
def ajax():
    return render_template("ajax.html")

@app.route('/_add_numbers')
def _add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

################--- END OF TESTING SCHEME ---############  

# Frank created this view to generate a page where users can create a session.
@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    centerA = 36.985
    centerB = -122.04
    if request.method == 'POST':
        data = db_manager.create_session(request.form['description'], request.form['location'], request.form['section'],
                                         request.form['start_time'], request.form['stop_time'], request.form['subject'],
                                         request.form['title'], request.form['host'], request.form['participants'],centerA,centerB)
        if data == db_manager.sessionError:
            error = 'You already have an active session with this title.'
            return render_template('add_listing.html',title='Create Session',form=None)
        else:
            return redirect(url_for('landing'))
    else:
        return render_template('add_listing.html',title='Create Session',form=None)


@app.route('/inbox')
def inbox():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        {
            'author': {'nickname': 'Frank'},
            'body': 'What are you talking about?'
            }, {
            'author': {'nickname': 'Bruno'},
            'body': 'I am the github scapegoat. cmon baby please work, it works'
            },
        {
            'author': {'nickname': 'Luc'},
            'body': ''}


        ]
    return render_template("inbox.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/landing')
def landing():
    testIP = '130.65.254.12'
    listings = models.Listings.query.all();
    name = 'hopey changy'
    lst = []
    for listing in listings:
        array = listing.stringArray()
        [lst.append(string) for string in array ]

    print(lst)
    match = geolite2.lookup(testIP)
    print(type(match))
    print(match.country)
    return render_template("landing.html",myName=name,listings=lst)


@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db_manager.user_validation(password,username):
            session['username'] = username
            return redirect(url_for('landing'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template("login3.html", error=error)
    return render_template("login3.html", error=error)

@app.route('/register', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        data = db_manager.create_user(email, password, username)
        if data == db_manager.usernameError:
            error = 'This username is taken.'
            return render_template('register.html', error = error)
        elif data == db_manager.emailError:
            error = 'This email is taken.'
            return render_template('register.html', error = error)
        else:
            return render_template('login3.html')

    else:
        return render_template('register.html')

@app.route('/profile')
def profile():
    return jsonify({'ip':request.remote_addr}), 200
    #return render_template("profileBEST.html")

