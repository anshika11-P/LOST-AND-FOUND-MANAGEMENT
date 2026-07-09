# LOST-AND-FOUND-MANAGEMENT
Lost & Found Management System

Project Overview

The Lost & Found Management System is a simple web application developed using Python Flask and SQLite. It helps users report lost and found items through an easy-to-use interface. Users can register, log in, report lost or found items, and view all submitted records.

Features

- User Registration
- User Login
- Dashboard
- Report Lost Item
- Report Found Item
- View Lost Items
- View Found Items
- Logout
- SQLite Database Integration

Technologies Used

- Python
- Flask
- HTML
- CSS
- SQLite

Project Structure

lost_found_project/
│── app.py
│── database.py
│── lostfound.db
│── requirements.txt
│── README.md
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── report_lost.html
│   ├── report_found.html
│   ├── lost_items.html
│   └── found_items.html
│
└── static/
    └── style.css

Installation

1. Clone the repository.
2. Open the project folder.
3. Install Flask:

pip install flask

4. Create the database:

python database.py

5. Run the project:

python app.py

6. Open your browser and visit:

http://127.0.0.1:5000

How It Works

1. Register a new account.
2. Log in using your registered email and password.
3. Open the dashboard.
4. Report lost or found items.
5. View all reported lost and found items.
6. Log out after completing your work.

Future Improvements

- Upload item images
- Search and filter items
- Email notifications
- Admin panel
- User profile management

Author
Anshika Passi

BCA Final Year Student

License

This project is created for educational and academic purposes.
