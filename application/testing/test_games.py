from testing.test_database import TestBase 
from flask import url_for 

class TestViews(TestBase): 
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertIn(b'Test Game List', response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_game(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_game(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code,200)

    
class TestCrud(TestBase): 
    def test_crud_add(self): 
        with self.client: 
            response = self.client.post(
                url_for('add'),
                data=dict(gameName="New Game Name", gameDescription="New Game Description", gameBook="New Game Book"),
                follow_redirects=True
            )
            self.assertIn(b'New Game', response.data)
    
    def test_crud_update(self):
        response = self.client.post(
            url_for('update', id=1),
            data=dict(gameName="Change game Name", gameDescription="Change Game Description", gameBook="Change Game Book"),
            follow_redirects=True
        )
        self.assertIn(b'Change Game', response.data)
    
    def test_crud_delete(self):
        response = self.client.get(url_for('delete', id=1))
        self.assertNotIn(response.data, b'Test Delete')
    

    
