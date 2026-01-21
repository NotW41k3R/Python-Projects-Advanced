# Flask Login System (Flask-WTF + Bootstrap5)

Completed on Day 60 & 61 of 100 Days of Python

A simple Flask project focused on building a functional login system using Flask-WTF for form handling. The app defines a `LoginForm` class with email and password fields, each validated using built-in WTForms validators. When the form is submitted, Flask-WTF automatically handles CSRF protection and checks required fields before the app processes the credentials.

The project renders pages using Jinja template inheritance, with all pages extending a shared `base.html` layout. Bootstrap5 is loaded through the extension, giving the app clean styling without writing custom CSS. 

On successful validation, the app checks for fixed “admin” credentials and displays either a success or denied page. The goal of this project was to understand how Flask manages forms, sessions, validation, and template organization in a real application structure.

Skills learned: Creating web forms using Flask-WTF, Adding field validators and handling form validation flow, Rendering forms manually and with Bootstrap form macros,  Understanding Jinja template inheritance (`extends`, `block`, `super`), Organizing multi-page Flask apps with clean HTML templates

Before using Flask-WTF, I built a simple HTML login form to understand how GET/POST methods work and how Flask interacts with forms. This version uses manual labels and input fields.
