from app import db, models
class db_manager(object):

    def get_users(self):
        return models.Logins.query.filter(models.Logins.username == 'embasa').first()

    def create_user(self, email, pwhash, username):
        #models.Logins.query.add(email, pwhash, username)
        #models.Logins.add(user)
        #models.Logins.commit()

    def create_session(self, description, location, section, start_time, stop_time, subject, title):
        pass

    def update_user(self, email, pwhash, username):
        pass

    def update_session(self, description, location, section, start_time, stop_time, subject, title):
        pass

    def user_validation(self, pwhash, username):
        pass

    def get_user_profile(self, username):
        pass

    def get_sessions(self):
        pass

name = db_manager()
print(name.get_users())
#name.create_user('poopy@poo.com', 'password', 'poo')
