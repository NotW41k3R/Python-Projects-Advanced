# Cafe & WiFi Directory (Flask + WTForms + CSV Storage)
Completed on Day 62 of 100 Days of Python

A Flask web application that lets users add cafes with details like location, Wi-Fi strength, and coffee rating, and displays them in a clean, Bootstrap-styled table. The project uses server-side validation with WTForms and stores submissions in a simple CSV file, making it a great intro to backend forms, templating, and lightweight data persistence.

When a user submits the “Add Cafe” form, the server validates all fields using WTForms validators. After successful validation, the data is appended to cafe-data.csv using Python’s file-handling. The cafe list page reads this CSV using Python’s csv module and renders it dynamically with Jinja2, looping through rows to generate the table.

Skills learned: Flask routing and project structure, WTForms server-side validation, Bootstrap5 form rendering, Using CSV as a lightweight database, Jinja2 templating, and building full-stack features (input → validation → storage → display)