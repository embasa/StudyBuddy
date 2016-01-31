from flask import Flask, render_template, redirect, url_for, request,session,escape
from app import app, models, db

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

# this is franks add listing form!
@app.route('/add_listing')
def add_listing():
    form = AddListingForm()
    return render_template('add_listing.html',title='Create Session',form=form)

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

@app.route('/login', methods =['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] !='admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('landing'))
    return render_template("login3.html", error=error)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile')
def profile():
    return render_template("profile2.html")

@app.route('/c/<username>')
def chicken(username):
    return 'User %s' % username
