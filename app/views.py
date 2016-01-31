import db_manager
from flask import Flask, render_template, redirect, url_for, request,session,escape
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

# Frank created this view to generate a page where users can create a session.
@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    if request.method == 'POST':
        data = db_manager.create_session(request.form['description'], request.form['location'], request.form['section'],
                                         request.form['start_time'], request.form['stop_time'], request.form['subject'],
                                         request.form['title'], request.form['host'], request.form['participants'])
        if data == 'session exists':
             error = 'You already have an active session with this title.'
        else:
            return redirect(url_for('landing'))


    form = AddListingForm()
    if form.validate_on_submit():
        flash('Login requested in order to create a new session!')
        return redirect('/login')
    return render_template('add_listing.html',title='Create Session',form=form)

# Frank created this method as a placeholder to actually create the session.
@app.route('/after_add_listing', methods=['GET', 'POST'])
def after_add_listing():
    error = None
    if request.method == 'POST':
        data = db_manager.create_session(request.form['description'], request.form['location'], request.form['section'],
                                         request.form['start_time'], request.form['stop_time'], request.form['subject'],
                                         request.form['title'], request.form['host'], request.form['participants'])
        if data == 'session exists':
             error = 'You already have an active session with this title.'
        else:
            return redirect(url_for('landing'))



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
    listings = models.Listings.query.all();
    name = 'hopey changy'
    if 'username' in session:
        #verify that it is valid username
        name = session['username']
    else:
        return redirect(url_for('login'))
    return render_template("landing.html",myName=name,listings=listings)

@app.route('/login2')
def login2():
    return render_template("login2.html")


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
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        if db_manager.create_user(email, password, username) == True:
            return redirect(url_for('login'))
        else:
            return render_template('register.html')
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template("profileBEST.html")

@app.route('/c/<username>')
def chicken(username):
    return 'User %s' % username
