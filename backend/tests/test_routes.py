import unittest
from app import create_app, db
from app.models import Recipe

class RecipeRoutesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()
            recipe = Recipe(title='Test Recipe', ingredients='Ingredient1, Ingredient2', instructions='Mix ingredients.')
            db.session.add(recipe)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_get_recipes(self):
        response = self.client.get('/api/recipes')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Recipe', response.data)

if _name_ == '_main_':
    unittest.main()