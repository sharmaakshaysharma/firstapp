// static/my_app/js/edit_product.js

document.addEventListener('DOMContentLoaded', function () {
    // When the modal is about to show, populate the form with data
    const modal = document.getElementById('EditProductModal');
    if (modal) {
        modal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget; // The button that triggered the modal
            const productId = button.getAttribute('data-product-id');
            const productTitle = button.getAttribute('data-product-title');
            const productAuthor = button.getAttribute('data-product-author');
            const productISBN = button.getAttribute('data-product-isbn');
            const productDescription = button.getAttribute('data-product-description');
            const productPrice = button.getAttribute('data-product-price');
            const productImage = button.getAttribute('data-product-image');

            // Fill the form fields with data
            document.getElementById('productTitle').value = productTitle;
            document.getElementById('productAuthor').value = productAuthor;
            document.getElementById('productISBN').value = productISBN;
            document.getElementById('productDescription').value = productDescription;
            document.getElementById('productPrice').value = productPrice;
            document.getElementById('productImage').value = productImage;

            // Set the form's action URL dynamically (if required)
            const form = document.getElementById('editProductForm');
            form.setAttribute('data-product-id', productId);  // Store product ID in the form
        });

        // Handle form submission via AJAX
        const form = document.getElementById('editProductForm');
        if (form) {
            form.addEventListener('submit', function (event) {
                event.preventDefault();  // Prevent the form from submitting the traditional way

                const formData = new FormData(this);
                const productId = this.getAttribute('data-product-id'); // Get product ID from form

                // Use fetch to send the form data via AJAX
                fetch(`/your-django-url-to-handle-edit/${productId}/`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // CSRF Token
                    }
                })
                .then(response => response.json()) // Assuming server returns JSON
                .then(data => {
                    if (data.success) {
                        // Successfully updated the product, do something, like closing the modal
                        alert('Product updated successfully!');
                        $('#EditProductModal').modal('hide');  // Close the modal
                        // Optionally, update the page with the new product data without reloading
                    } else {
                        // Show error message if something went wrong
                        alert('Failed to update the product. Please try again.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while updating the product.');
                });
            });
        }
    }
});
