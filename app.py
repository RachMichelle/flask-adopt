from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'adoptionapp'

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """home page with pet list"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/pets/<pet_id>')
def show_pet_info(pet_id):
    """show details for pet with associated id"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet-info.html', pet=pet)

@app.route('/pets/add', methods = ['GET', 'POST'])
def new_pet_form():
    """show or submit new pet form"""

    form=PetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        age=form.age.data
        notes=form.notes.data

        if form.photo_url.data == '':
            photo_url=None
        else:
            photo_url=form.photo_url.data


        pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f'{pet.name} was added!')
        return redirect('/')
    
    else:
        return render_template('new-pet-form.html', form=form)

@app.route('/pets/<pet_id>/edit', methods =['GET', 'POST'])
def edit_pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return f"Viewing edit page for {pet.name}, id {pet.id}"
