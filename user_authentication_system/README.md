# User Authentication System (Flask + Flask-Login)
Completed on Day 68 of 100 Days of Python

A full user authentication system built using Flask, integrating registration, login, session management, and protected routes. The application stores user information in an SQLite database through SQLAlchemy ORM and handles password hashing and salting securely using Werkzeug.

The project sets up a custom `User` model using SQLAlchemy’s `DeclarativeBase` along with `flask_login`’s `UserMixin` to bridge database users with Flask-Login’s session system. During registration, the app checks whether the email already exists; if not, it hashes the password and saves the new user. Logged-in users are recognized across pages via Flask-Login’s session handling.

The login flow validates the email, compares the submitted password hash with the stored hash, and logs the user into a session. Protected routes use `@login_required`, ensuring only authenticated users can access pages like the “secrets” area or download restricted files. Logout instantly clears the session and redirects the user back to the homepage.

Skills learned: user authentication flow design, secure password hashing and verification, session handling with Flask-Login, protecting routes with decorators, handling login state inside templates, form validation logic, managing user sessions across requests, and building a complete authentication workflow from scratch.