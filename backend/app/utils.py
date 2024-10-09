def format_recipe(recipe):
    return {
        "id": recipe.id,
        "title": recipe.title,
        "ingredients": recipe.ingredients,
        "instructions": recipe.instructions
    }