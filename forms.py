"""forms for adoption page"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class PetForm(FlaskForm):
    """form to add a new pet"""

    name = StringField("Pet Name", 
                       validators=[InputRequired(message='Name cannot be blank')])
    species = StringField("Species", 
                          validators=[AnyOf(['Dog', 'Cat', 'Rabbit', 'Bird'], message='Must be a Dog, Cat, Rabbit, or Bird.')]) 
    photo_url = StringField("Photo", 
                            validators=[URL(), Optional()])
    age = IntegerField("Pet Age",
                       validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """form to edit an existing pet--same as add form but has option to change pet availability"""

    available = BooleanField("Is Available")
    name = StringField("Pet Name", 
                       validators=[InputRequired(message='Name cannot be blank')])
    species = StringField("Species", 
                          validators=[AnyOf(['Dog', 'Cat', 'Rabbit', 'Bird'], message='Must be a Dog, Cat, Rabbit, or Bird.')]) 
    photo_url = StringField("Photo", 
                            validators=[URL(), Optional()])
    age = IntegerField("Pet Age",
                       validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])