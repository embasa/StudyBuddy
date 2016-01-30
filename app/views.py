from flask import render_template
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
            },
        {
            'author': {'nickname': 'Bruno'},
            'body': 'I am the github scapegoat. cmon baby please work, it works'
            }
        ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route('/login2')
<<<<<<< HEAD
def login2():
=======
def login():
>>>>>>> c6e90163f975aa65a86aa0ddecffce57ce093d33
    return render_template("login2.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")
