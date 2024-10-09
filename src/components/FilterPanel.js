const FilterPanel = ({onFilterChange}) => {
  const handleChange = e => {
    onFilterChange(e.target.value)
  }

  return (
    <div className="filter-panel">
      <label htmlFor="filter">Filter by Ingredients:</label>
      <input
        type="text"
        id="filter"
        placeholder="Enter ingredient..."
        onChange={handleChange}
        className="filter-input"
      />
    </div>
  )
}

export default FilterPanel
