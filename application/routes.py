from flask import render_template, url_for, redirect, request
from sqlalchemy.engine import url
from application import app, db 
from application.models import CharacterInformation, GameInformation
from application.form import CharacterInformationForm, GameInformationForm

@app.route('/', methods=['POST', 'GET'])
def index(): 
    games = GameInformation.query.all()
    return render_template('index.html', title="Game List App", games=games)

@app.route('/add', methods=['POST','GET'])
def add(): 
    form = GameInformationForm()
    if form.validate_on_submit(): 
        games = GameInformation(
            gameName = form.gameName.data,
            gameDescription = form.gameDescription.data,
            gameBook = form.gameBook.data
        )
        db.session.add(games)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new Game", form=form)
    
@app.route('/complete/<int:game_id>')
def complete(game_id):
    games = GameInformation.query.get(game_id)
    games.gameCompleted = True 
    return redirect(url_for('index'))

@app.route('/update/<int:game_id>', methods=['GET','POST'])
def update(game_id):
    form = GameInformationForm()
    games = GameInformation.query.get(game_id)
    if form.validate_on_submit(): 
        games.gameName = form.gameName.data
        games.gameDescription = form.gameDescription.data
        games.gameBook = form.gameBook.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.gameName.data = games.gameName
        form.gameDescription.data = games.gameDescription
        form.gameBook.data = games.gameBook
    return render_template('update.html', title="Update your Game", form=form)

@app.route('/delete/<int:game_id>')
def delete(game_id): 
    games = GameInformation.query.get(game_id)
    db.session.delete(games)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/character', methods=['POST', 'GET'])
def characterindex():
    characters = CharacterInformation.query.all()
    return render_template('characterindex.html', title="Character List App", characters=characters)

@app.route('/addcharacter', methods=['POST', 'GET'])
def addcharacter():
    form = CharacterInformationForm()
    if form.validate_on_submit():
        characters = CharacterInformation(
            characterName = form.characterName.data,
            characterRace = form.characterRace.data,
            characterClass = form.characterClass.data 
        )
        db.session.add(characters)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addCharacter.html', title="Add a new Character", form=form)

@app.route('/deletecharacter/<int:character_id>')
def deletecharacter(character_id):
    characters = CharacterInformation.query.get(character_id)
    db.session.delete(characters)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/updatecharacter/<int:character_id>', methods=['GET','POST'])
def updatecharacter(character_id):
    form = CharacterInformationForm()
    characters = CharacterInformation.query.get(character_id)
    if form.validate_on_submit():
        characters.characterName = form.characterName.data
        characters.characterRace = form.characterRace.data 
        characters.characterClass = form.characterClass.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.characterName.data = characters.characterName
        form.characterRace.data = characters.characterRace 
        form.characterClass.data = characters.characterClass
    return render_template('updatecharacter.html', title="Update your characters", form=form)
