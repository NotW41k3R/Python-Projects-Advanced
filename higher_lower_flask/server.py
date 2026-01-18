from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
    "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

number = random.randint(0,9)
# print(number)

@app.route(f"/<int:guess>")
def correct_number(guess):
    # print(guess)
    if guess < number:
        return "<h1>Too Low, Try Again</h1>"\
        "<img src=https://preview.redd.it/guys-i-need-max-verstappen-memes-ive-got-no-verstappen-v0-zvuz82xoua5e1.jpeg?auto=webp&s=dfe16a5b15f7fd0a59b521eec73ddbdf0c1efd3c width=700>"
    elif guess > number:
        return "<h1>Too High, Try Again</h1>"\
        "<img src=https://media.tenor.com/OQVw3E8GjtkAAAAe/nerd-max-verstappen.png width=700>"
    else:
        return "<h1>That's it</h1>"\
        "<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHl7Ctyr2q9bVsvePiSqvWQ6bdIUXN_klUZQ&s width=700>"
    
if __name__ == "__main__":
    app.run(debug=True)