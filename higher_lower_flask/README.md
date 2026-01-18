# Number Guessing Game (Flask Web App)
Completed on Day 55 of 100 Days of Python

A simple interactive web based number guessing game built using Flask. The application generates a random number between 0 and 9 when the server starts and challenges the user to guess it through the browser by visiting different URLs.

The home route (`/`) displays instructions and a GIF prompting the user to guess a number. Each guess is made by navigating to `/<guess>`, where Flask captures the integer from the URL. The server compares the user’s guess with the randomly generated number and responds with feedback, indicating whether the guess is too low, too high, or correct.

Skills learned: Flask app setup and routing, dynamic URL parameters, basic backend logic, Python conditionals, handling type conversion in web routes, understanding decorators (`@app.route`), and working with `*args` / `**kwargs` concepts.
