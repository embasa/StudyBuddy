from app import db, models
class db_manager(object):
    emailError = 'email'
    usernameError = 'username exists'
    dneError = 'not found'
    inSessionError = 'already added'
    sessionError = 'session exists'
    pwError = 'invalid password'

    def get_user(self, username):#returns user matching username or None
        return models.Logins.query.filter(username == username).first()

    def get_participants(self, title, host):#returns participants in session(match:host&title) or none
        return models.ActiveSessions.query.filter(title == title, host == host)

    def create_user(self, email, pwhash, username): 
        usernames = models.Logins.query.all()
        for user in usernames:
            if user.username == username:               
                return self.usernameError
            if user.email == email:
                return self.emailError
        user = models.Logins(email, pwhash, username)
        db.session.add(user)
        db.session.commit()
        return True
        
    def create_session(self, description, location, section, start_time, stop_time, subject, title, host, participants):
        sessions = models.Listings.query.all()
        for session in sessions:
            if session.host == host and session.title == title:
                return self.sessionError
        session = models.Listings(description, location, section, start_time, stop_time, subject, title, host, participants)
        db.session.add(session)
        db.session.commit()
        return True

    def add_participant(self, new_participant, title, host):#verify new participant exists
        user = self.get_user(new_participant)
        if user is None:
            return self.dneError
        else: #verify participant is not already in session
            participants = self.get_participants(title, host)
            if participants is not None:#if not empty check entries
                for existingparticipant in participants:
                    if existingparticipant == new_participant:#if already in session avoids duplicate entry
                        return self.inSessionError
            participant = models.ActiveSessions(new_participant, title, host)
            db.session.add(participant)
            db.session.commit()
            return True

    def delete_user(self, username): 
        user = models.Logins.query.filter(username == username).first()
        db.session.delete(user)
        db.session.commit()

    def delete_session(self, title, host):#add host to make unique 
        session = models.Listings.query.filter(title == title, host == host).first()
        participants = self.get_participants(session.title, session.host)
        if participants is not None:
            for participant in participants:
                self.delete_participant(participant.participant, participant.title, participant.host)
        db.session.delete(session)
        db.session.commit()
    
    def delete_participant(self, participant, title, host):
        participant = models.ActiveSessions.query.filter(participant == participant, title == title, host == host).first()
        db.session.delete(participant)
        db.session.commit()

    
    def user_validation(self, pwhash, username):#verifies user's credentials
        userCheck = self.get_user(username)
        if userCheck is None:
            return self.dneError
        elif userCheck.pwhash != pwhash:
            return self.pwError
        else:
            return True
        
