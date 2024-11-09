
# Django Social Media Web Application

## Project Overview

This project is a Django-based social media web application designed for users to express their opinions, thoughts, and ideas on various topics. The application provides essential social media features, allowing users to interact with one another and perform various CRUD (Create, Read, Update, Delete) operations on their posts. The platform encourages opinion sharing and engagement through an interactive commenting system and robust user authentication.

## Features

1. **User Authentication**:
   - Secure user registration, login, and logout functionality.
   - Only authorized users can access, create, or modify content on the platform.

2. **CRUD Operations**:
   - Users can create, read, update, and delete their posts.
   - Easy-to-navigate interface for viewing and managing content.

3. **Commenting System**:
   - Users can comment on each other’s posts, encouraging community interaction and discussions.
   - Comments can be created, read, and deleted, allowing dynamic conversations.

4. **Like/Dislike System**: 
   - Implement a like/dislike feature to allow users to react to posts.

5. **Opinion Posting**:
   - The platform is specifically designed for users to post their thoughts and opinions on a wide range of topics.
   - Users can freely express themselves and engage in meaningful exchanges.

## Tools and Technologies

- **Django**: Web framework for developing the server-side of the application.
- **SQLite**: Default database used for development (can be replaced with other databases like PostgreSQL or MySQL).
- **HTML/CSS**: For front-end structure and styling.
- **JavaScript**: To add interactive features to the front-end.

## Project Structure

The project follows Django's default structure with additional folders for templates and static files.


## Setup and Installation

1. **Clone the repository** and navigate to the project directory:

   ```bash
   git clone https://github.com/Pr45H4nt/SaySomething.git
   cd socialmediaweb
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations** to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application** at `http://127.0.0.1:8000` in your web browser.

## Usage

- **Register**: Users can create an account by registering on the platform.
- **Login**: Once registered, users can log in to access features like posting and commenting.
- **Post**: Users can create new posts, edit their existing posts, or delete them.
- **Comment**: Users can comment on other users' posts to engage in discussions.
- **Logout**: Users can securely log out when done.

## Future Enhancements
- **Notification System**: Add notifications for new comments or interactions on user posts.
- **Profile Customization**: Allow users to add profile pictures and bio information.

## Author

Prashant Paneru

