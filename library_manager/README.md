# Personal Library Manager (Flask + SQLite + SQLAlchemy)

A simple Flask web app built to understand how databases actually work in projects and to practice CRUD operations using SQL concepts through SQLAlchemy.

The app lets you add books with a title, author, and rating. You can view the entire list, update a book’s rating, or delete a book completely. Every one of these actions interacts with an SQLite database

When a user submits the “Add Book” form, WTForms validates the fields and the new entry is added to the database through SQLAlchemy. The home page reads the data by selecting all rows from the Book table and displays them using Jinja2. Editing a rating loads the book, updates the value, and commits the change. Deleting a book removes the row from the database and redirects back to the updated list.

Skills learned: SQL fundamentals, SQLAlchemy model and schema definition, CRUD (Create/Read/Update/Delete) operations, Flask routing and templating, WTForms server-side validation, Jinja2 loops and structure, and building a complete backend workflow using a real database instead of CSV or in-memory data.
