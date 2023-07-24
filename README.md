# VoltAutoWebsite
This is a web application built with Django that allows users to manage and view information about electric cars. The application was developed as part of a project to learn Django and web development.

## Features

1. **User Authentication**: Users can create an account, login, logout, and view their profile.
2. **Car Management**: Registered users can add new electric cars to the database, providing details such as the model, automaker, description, price, battery capacity, range per charge, and an image.
3. **Car View**: All users can view the list of cars in the database and click on a car to view more details.
4. **Commenting**: Logged-in users can write comments on the detail page of each car.
5. **Seller View**: All users can view a list of sellers (users who have added cars).

## Installation

1. Clone this repository.
2. Install the requirements using `pip install -r requirements.txt`.
3. Run the server with `python manage.py runserver`.

## Usage

Visit `http://localhost:8000` in your web browser to view the app.

## Future Enhancements

- Implement a search feature to allow users to search for cars by model or automaker.
- Allow users to edit and delete the cars they have added.
- Add user roles and permissions to manage access to certain features.
- Improve the UI/UX with a more sophisticated front-end framework or library.
