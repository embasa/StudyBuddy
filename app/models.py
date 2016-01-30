from app import db

class Logins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True, unique=True)
    pwhash = db.Column(db.String(100), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
        email = '<email: %r >' % (self.email)
        pwhash = 'pwhash: %r >' % (self.pwhash)
        username = 'username: %r >' % (self.username)
        return email + ' ' + pwhash + ' ' + username

class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(60), index=True, unique=True)
    subject = db.Column(db.String(20), 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r >' % (self.nickname)
