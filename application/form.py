from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import GameInformation
from application.models import CharacterInformation

class GameInformationForm(FlaskForm):
    gameName = StringField('GameName', 
        validators = [
            DataRequired()
        ]
    )

    gameDescription = StringField('GameDescription',
        validators=[
            DataRequired()
        ]
    ) 

    gameBook = StringField('GameBook',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Game Creation')

    def validate_game(self, gameName):
        all_games = GameInformation.query.all()
        if gameName.data in all_games:
            raise ValidationError('You already have that Game')

# Character Form
class CharacterInformationForm(FlaskForm):
    characterName = StringField('CharacterName', 
        validators = [
            DataRequired()
        ]
    )

    characterRace = StringField('CharacterRace',
        validators=[
            DataRequired()
        ]
    ) 

    characterClass = StringField('CharacterClass',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Character Creation')

    def validate_game(self, characterName):
        all_characters = GameInformation.query.all()
        if characterName.data in all_characters:
            raise ValidationError('You already have that Game')