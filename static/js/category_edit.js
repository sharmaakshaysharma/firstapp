// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get all the 'Edit' links that trigger the modal
    const editLinks = document.querySelectorAll('[data-bs-toggle="modal"][data-bs-target="#EditCategoryModel"]');

    // Loop through each link and add an event listener to populate the modal
    editLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Get category ID and Name from the data-* attributes
            const categoryId = this.getAttribute('data-category-id');
            const categoryName = this.getAttribute('data-category-name');

            // Populate the modal fields with the retrieved values
            const categoryIdInput = document.getElementById('categoryId');
            const categoryNameInput = document.getElementById('categoryName');

            // Set the values in the modal inputs
            categoryIdInput.value = categoryId;  // Set category ID to the hidden field
            categoryNameInput.value = categoryName;  // Set category Name to the input field
        });
    });
});
