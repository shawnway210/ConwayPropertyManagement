Property Management Application README
Introduction
Welcome to the Property Management Application! This application allows users to manage properties, reviews, and images. Users can sign up, log in, and perform various actions based on their roles (Admin or Visitor). The application is built using Flask for the backend and React for the frontend.

Getting Started
Follow these steps to set up and run the application on your local machine:

Backend
Navigate to the backend directory.

Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
The backend will be accessible at http://localhost:5555.

Frontend
Navigate to the frontend directory.

Install the required npm packages:

bash
Copy code
npm install
Run the React application:

bash
Copy code
npm start
The frontend will be accessible at http://localhost:3000.

Features
Authentication
Users can sign up, log in, and log out.
Different user roles (Admin, Visitor) determine access permissions.
Properties
Admins can view, add, and delete properties.
Visitors can view a list of properties.
Reviews
Users can view and add reviews for specific properties.
Admins can manage reviews by editing or deleting them.
Images
Admins can add and delete images associated with properties.
Project Structure
The project is organized into frontend (React) and backend (Flask) directories. Here's an overview of each directory:

Frontend
Components: React components for different parts of the application (e.g., Properties, Reviews, Images).
Contexts: Contains the DarkModeContext used for dark mode styling.
CSS: Stylesheets for styling the components.
Pages: React components representing different pages in the application (e.g., Login, Signup, Properties).
SiteTitle.js: React component for displaying the site title.
index.css: Global styles for the application.
Backend
app.py: Flask application entry point.
config.py: Configuration settings for the Flask application.
models.py: SQLAlchemy models for User, Property, Review, Image, and PropertyUser.
routes.py: Flask routes for handling HTTP requests.
requirements.txt: List of Python packages required for the backend.
Contributing
If you'd like to contribute to this project, follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-name
Make your changes and commit them: git commit -m 'Description of changes'
Push to the branch: git push origin feature-name
Submit a pull request.
