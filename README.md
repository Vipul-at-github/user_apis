# User Registration API Documentation with Swagger

Welcome to the documentation for the User Registration API. This API handles user registration and authentication processes using Django.

## Features

- User Registration: Register new users with required information.
- User Authentication: Authenticate registered users.

## API Endpoints

All API endpoints are documented using Swagger, which provides a user-friendly interface for exploring and testing the API. You can access the Swagger documentation by running the project locally or deploying it to a web server.

## Running Locally

1. **Clone the Repository:**
git clone https://github.com/Vipul-at-github/user_apis.git

2. **Navigate to the Repository:**
cd user-registration-api

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the Server:**
python manage.py runserver

5. **Access Swagger Documentation:**
Open your web browser and navigate to `http://localhost:8000/swagger/` to access the Swagger UI. Here, you can explore and test the API endpoints.

## Swagger Implementation

The User Registration API documentation is generated using Django Rest Framework's built-in Swagger support. Here's how Swagger was integrated into the project:

1. **Django Rest Framework:**
The `djangorestframework` package is used to build the API, and it provides the Swagger UI out of the box.

2. **Integration:**
API endpoints are defined using Django Rest Framework's serializers and views. The Swagger UI is automatically generated from these definitions.

## API Documentation

You can access the API documentation using the Swagger UI at `http://localhost:8000/swagger/` when running the project locally. Alternatively, deploy the project to a web server to make the documentation accessible online.

## Contact

Feel free to reach out if you have any questions or feedback about the User Registration API. You can contact me at [manevip17@gmail.com](mailto:manevip17@gmail.com).

---

Thank you for using the User Registration API and exploring its documentation!
