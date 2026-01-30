# Blogsite - Full Capstone Overview (Parts 1-4)

A four-part capstone project that evolves from a simple API-powered blog viewer into a fully functional, REST-style blogging platform with user accounts. Each part builds on the previous one, gradually introducing new tools, architecture, and real-world backend concepts.

---

## Part 1 - Flask + REST API Rendering

A lightweight Flask app that fetches blog data from an external JSON API and displays it using Jinja templates. Each post is converted into a Python object for clean rendering.
Focus: consuming APIs, handling JSON, dynamic templating.

Skills: API requests, parsing JSON, routing with Flask, basic Jinja templates.

---

## Part 2 - Flask + Bootstrap + Jinja Layouts

This version adds Bootstrap styling and cleaner template structure. Blog data is still API-driven, but the site now includes a homepage, post pages, About, and Contact sections with consistent layouts.
Focus: frontend structure and styling.

Skills: Bootstrap integration, reusable Jinja layouts, multi-page site structure, responsive design.

---

## Part 3 - REST-Style CRUD + SQLAlchemy + CKEditor

The blog becomes a real content-management system. Posts are stored in an SQLite database, and users can create, edit, and delete posts. WTForms handles validation, and CKEditor provides rich text editing.
Routes follow REST-like patterns using different HTTP methods for different actions.
Focus: real database storage and CRUD functionality.

Skills: SQLAlchemy models, CRUD endpoints, WTForms validation, CKEditor, REST-style routing, Bootstrap UI.

---

## Part 4 - User Management System (Login + Registration)

This final stage adds authentication so only registered users can create, edit, or delete posts. Users can register, log in, and log out. Admin privileges can be introduced to restrict access to specific routes.
Focus: security, authentication, and role-based access.

Skills: Flask-Login, password hashing, protected routes, user sessions, admin-only features.

---

