# Cafe API (Flask + SQLAlchemy)
Completed on Day 68 of 100 Days of Python

A simple REST API built with Flask, SQLAlchemy, and SQLite to manage a database of cafés.
It supports full CRUD operations: get random cafés, list all cafés, search by location, add new entries, update prices, and delete cafés with an API key.

The app uses SQLAlchemy’s ORM system to define a Cafe model with fields such as name, location, amenities, and coffee price. Each café record is represented as a Python object mapped to rows in a SQLite database.

Skills learned: designing REST APIs, structuring Flask routes, working with SQLAlchemy ORM models, database querying (`select()`, `scalars()`), converting ORM objects to JSON, handling form data vs query parameters, implementing PATCH and DELETE methods, and applying basic API-key-based access control.