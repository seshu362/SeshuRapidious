const SearchBar = ({searchTerm, onSearchChange, onSearchClick}) => (
  <div className="search-bar-container">
    <input
      type="text"
      placeholder="Search Recipes..."
      className="search-bar"
      value={searchTerm}
      onChange={onSearchChange}
    />
    <button onClick={onSearchClick} className="search-button">
      Search
    </button>
  </div>
)

export default SearchBar
