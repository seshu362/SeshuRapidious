from marshmallow import Schema, fields

class RecipeSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    ingredients = fields.Str()
    instructions = fields.Str()