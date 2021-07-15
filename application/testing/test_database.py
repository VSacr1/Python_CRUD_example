import unittest 
from flask import url_for 
from flask_testing import TestCase 

from application import app,db 
from application.models import GameInformation

class TestDatabase(TestCase):
    def create_application(self): 
        app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"
        app.config['SECRET_KEY']='this is a secret key'
        app.config['DEBUG']=True 
        app.config['WTF_CSRF_ENABLED'] = False 
        return app 

    def setUp(self):
        db.create_all()

        sample1 = GameInformation(gameName="Test name", gameDescription="Test Description", gameBook="Test Book")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self): 
        db.session.remove()
        db.drop_all()