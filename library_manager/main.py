from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# App initialisation
app = Flask(__name__)
app.secret_key = "hfvsfvetwgfsdhblggdf4gdf5gdf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# For rendering form
bootstrap = Bootstrap5(app)

# Forms
class BookForm(FlaskForm):
    title = StringField(label='Book Name', validators=[DataRequired()])
    author = StringField(label='Book Author', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    submit = SubmitField(label='Add Book')

class RatingForm(FlaskForm):
    new_rating = FloatField(label='New Rating', validators=[DataRequired()])
    submit = SubmitField(label='Update Rating')

# Database initialisation 
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Database Schema
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

# Endpoints
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books = all_books)

@app.route("/add", methods=['POST', 'GET'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        new_book = Book(
            title = book_form.title.data,
            author = book_form.author.data,
            rating = book_form.rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form = book_form)

@app.route('/edit/<int:book_id>', methods = ['POST', 'GET'])
def edit(book_id):
    rating_form = RatingForm()
    book_to_edit = db.get_or_404(Book, book_id)
    if rating_form.validate_on_submit():
        book_to_edit.rating = rating_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home')) 
    return render_template('edit.html', form = rating_form, book = book_to_edit)

@app.route('/delete/<int:book_id>', methods=['GET','POST'])
def delete(book_id):
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)


# Database creation without sqlalchemy
# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, " \
# #                 "title varchar(250) NOT NULL UNIQUE, " \
# #                 "author varchar(250) NOT NULL, " \
# #                 "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
