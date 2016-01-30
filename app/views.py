from flask import Flask, render_template, redirect, url_for, request
from app import app

@app.route('/')
@app.route('/index')

def index():
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
            }
        ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/landing')
def landing(name):
    return render_template("landing.html",myName=name)

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
            return redirect(url_for('landing'),myName='randomness')
    return render_template("login3.html", error=error)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/c/<username>')
def chicken(username):

    return 'User %s' % username
