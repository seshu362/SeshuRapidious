import unittest
from app import create_app, db
from app.models import Recipe

class RecipeModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_recipe_creation(self):
        with self.app.app_context():
            recipe = Recipe(title='Test Recipe', ingredients='Ingredient1, Ingredient2', instructions='Mix ingredients.')
            db.session.add(recipe)
            db.session.commit()
            self.assertEqual(recipe.id, 1)
            self.assertEqual(recipe.title, 'Test Recipe')

    def test_recipe_str(self):
        recipe = Recipe(title='Test Recipe', ingredients='Ingredient1', instructions='Instructions')
        self.assertEqual(str(recipe), 'Test Recipe')

if _name_ == '_main_':
    unittest.main()