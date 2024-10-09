const RecipeCard = ({recipe}) => (
  <div className="recipe-card">
    <h3>{recipe.title}</h3>
    <p>{recipe.ingredients}</p>
    <p>{recipe.instructions}</p>
  </div>
)

export default RecipeCard
