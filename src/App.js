import {useEffect, useState} from 'react' // No need to import React in newer versions
import Header from './components/Header'
import RecipeCard from './components/RecipeCard'
import SearchBar from './components/SearchBar'
import fetchRecipes from './services/api' // Correct for default export

import './App.css'

function App() {
  const [recipes, setRecipes] = useState([])
  const [searchTerm, setSearchTerm] = useState('') // Manage search term
  const [error, setError] = useState(null) // Manage error state

  // Query parameters for fetching recipes
  const filters = {
    cuisine: 'Italian', // Example filter
    ingredients: 'tomato',
    prepTime: '30',
  }
  const page = 1 // Example page number
  const limit = 10 // Example limit

  useEffect(() => {
    const loadRecipes = async () => {
      try {
        const data = await fetchRecipes(searchTerm, filters, page, limit) // Fetch with filters
        setRecipes(data) // Store the fetched recipes
      } catch (fetchError) {
        // Use a different name to avoid shadowing
        setError(fetchError.message) // Set error state to display
      }
    }

    loadRecipes()
  }, [searchTerm]) // Fetch recipes when search term changes

  const handleSearchChange = event => {
    setSearchTerm(event.target.value) // Update search term state
  }

  const filteredRecipes = recipes.filter(
    recipe => recipe.title.toLowerCase().includes(searchTerm.toLowerCase()), // Adjust according to your data structure
  )

  return (
    <div className="App">
      <Header />
      <SearchBar searchTerm={searchTerm} onSearchChange={handleSearchChange} />
      {error && <p>Error: {error}</p>} {/* Display error message if present */}
      <div className="recipe-list">
        {filteredRecipes.map(recipe => (
          <RecipeCard key={recipe.id} recipe={recipe} /> // Ensure recipe.id exists
        ))}
      </div>
    </div>
  )
}

export default App
