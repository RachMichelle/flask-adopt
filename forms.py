"""forms for adoption page"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class PetForm(FlaskForm):

    name = StringField("Pet Name", 
                       validators=[InputRequired(message='Name cannot be blank')])
    species = StringField("Species", 
                          validators=[AnyOf(['Dog', 'Cat', 'Rabbit', 'Bird'])]) 
    photo_url = StringField("Photo", 
                            validators=[URL(), Optional()])
    age = IntegerField("Pet Age",
                       validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])