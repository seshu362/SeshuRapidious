// api.js
const BASE_URL = 'http://localhost:5000/api'

const fetchRecipes = async (query, filters, page, limit) => {
  const params = new URLSearchParams({
    q: query,
    cuisine: filters.cuisine,
    ingredients: filters.ingredients,
    prep_time: filters.prepTime,
    page,
    limit,
  })

  try {
    const response = await fetch(
      `${BASE_URL}/recipes/search?${params.toString()}`,
    )

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error fetching recipes:', error)
    throw error // Rethrow the error to handle it in the component
  }
}

export default fetchRecipes
