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
            'body': 'I am the github scapegoat. cmon baby please work'
            }
        ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

