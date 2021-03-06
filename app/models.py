from app import db

class Logins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True, unique=True)
    pwhash = db.Column(db.String(100), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)

    def __init__(self,email,pwhash,username):
        self.email = email
        self.pwhash = pwhash
        self.username = username

    def __repr__(self):
        email = '<email: %r >' % (self.email)
        pwhash = 'pwhash: %r >' % (self.pwhash)
        username = 'username: %r >' % (self.username)
        return email + ' ' + pwhash + ' ' + username

class Listings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), index=True, unique=True)
    location = db.Column(db.String(60), index=True, unique=True)
    section = db.Column(db.String(60), index=True, unique=True)
    start_time = db.Column(db.String(60), index=True, unique=True)
    stop_time = db.Column(db.String(60), index=True, unique=True)
    subject = db.Column(db.String(60), index=True, unique=True)
    title = db.Column(db.String(60), index=True, unique=True)
    host = db.Column(db.String(60), index=True, unique=True)
    participants = db.Column(db.String(200), index=True, unique=True)
    latitude = db.Column(db.Integer, index=True,unique=False)
    longitude = db.Column(db.Integer, index=True,unique=False)

    def __init__(self, description, location, section, start_time, stop_time, subject, title,host,participants,latitude,longitude):
        self.description = description
        self.location = location
        self.section = section
        self.start_time = start_time
        self.stop_time = stop_time
        self.subject = subject
        self.title = title
        self.host = host
        self.participants = participants
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        description = 'Description: %r' % str(self.description)
        location = '%s' % str(self.location)
        section = 'Section: %r' % str(self.section)
        start_time = 'Start Time: %r' % str(self.start_time)
        stop_time = 'Stop Time: %r' % str(self.stop_time)
        subject = '%s' % str(self.subject)
        title = '%s' % str(self.title)
        host = 'Host: %r' % str(self.host)
        participants = 'Participants: %r' % str(self.participants)
        latitude = 'latitude: %r' % str(self.latitude)
        longitude = 'longitude: %r' % str(self.longitude)
        return str(title + ' ' + location + '\n'
                + subject + ' ' + section + '\n'
                + start_time + ' ' + stop_time + '\n'
                + description + ' ' + host + '\n'
                + participants + ' ' + latitude + '\n'
                + longitude)
    
    def stringArray(self):
        location = '%s' % str(self.location)
        subject = '%s' % str(self.subject)
        title = '%s' % str(self.title)
        return [title,subject,location]
               
class ActiveSessions(db.Model):
    __tablename__ = 'ActiveSessions'
    id = db.Column(db.Integer, primary_key=True)
    participant = db.Column(db.String(60), index=True, unique=False)
    title = db.Column(db.String(60), index=True, unique=False)
    host =  db.Column(db.String(60), index=True, unique=False)

    def __init__(self,participant,title,host):
        self.participant = participant
        self.title = title
        self.host = host

    def __repr__(self):
        participant = '<Participant: %r >' % (self.participant)
        title = 'title: %r >' % (self.title)
        host = 'host: %r >' % (self.host)
        return participant + ' ' + title + ' ' + host

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r >' % (self.nickname)

