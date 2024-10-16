from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connect to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet object model"""

    __tablename__='pets'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)

    name=db.Column(db.Text, nullable=False)

    species=db.Column(db.Text, nullable=False)
    
    photo_url=db.Column(db.Text, default='https://t3.ftcdn.net/jpg/01/63/12/16/360_F_163121616_76WYhq1hFN5B3BJYfASSp9ekLUBWUvhR.jpg')

    age=db.Column(db.Integer)

    notes=db.Column(db.Text)

    available=db.Column(db.Boolean, nullable=False, default=True)