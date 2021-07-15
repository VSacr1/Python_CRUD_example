from application import db 

class GameInformation(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    gameName = db.Column(db.String(30))
    gameDescription = db.Column(db.String(30))
    gameBook = db.Column(db.String(30))
    gameCompleted = db.Column(db.Boolean, default=False)

class CharacterInformation(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    characterName = db.Column(db.String(30))
    characterRace = db.Column(db.String(30))
    characterClass = db.Column(db.String(30))