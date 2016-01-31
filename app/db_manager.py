from app import db

def view_users():
    return models.Logins.query.all()
