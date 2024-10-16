from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'bloglyapp'

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """home page with pet list"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)