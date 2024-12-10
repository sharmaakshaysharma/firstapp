Ecomm Bookstore 📚
An e-commerce platform for books, allowing users to browse categories, view products, add items to their cart, and make purchases. This project is built using Django and Bootstrap for a responsive and user-friendly interface.
Also integrate google book api , Gemini AI .
And also Open Authentication.

Features 🚀
User Authentication: Register, log in, log out, and manage user accounts.

Product Management:
View product details in a modal.
Add items to the cart.
Dynamic cart icon updates in the navbar.
Terms and Conditions Modal: Users must agree before registration.
Prerequisites 🛠️
Ensure the following are installed:

Python 3.12
Django 4.2
Bootstrap 5 (for front-end styling)
SQLite (default database for Django)
Installation ⚙️
Clone the Repository
bash
Copy code
git clone (https://github.com/sharmaakshaysharma/firstapp.git)
cd ecomm-bookstore
Install Dependencies

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser
bash
Copy code
python manage.py createsuperuser
Run the Server
bash
Copy code
python manage.py runserver
