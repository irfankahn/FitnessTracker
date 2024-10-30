# Fitness Tracker

A full-stack fitness tracking application built with Python, Django, React, and SQLite. This app allows users to manage their workouts, set fitness goals, and track their progress in a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### User Authentication and Management
- **User Registration**: Users can create accounts by registering with a username, password, and personal fitness goals.
- **User Login**: Users can log in using their credentials to access their profile.
- **User Logout**: Users can log out, invalidating their session.

### Workout Tracking
- **Create Workouts**: Users can log their workouts, specifying the type of workout (e.g., running, cycling), duration (in minutes), and calories burned.
- **View Workouts**: Users can view a list of all workouts they have logged.
- **User-Specific Workouts**: Users can see only their workouts, allowing for personalized tracking.
- **Workout Details**: Users can access details of individual workouts to review specific information about each session.

### Data Storage
- **SQLite Database**: User and workout information is stored in a SQLite database, allowing for easy management and retrieval of data.

### RESTful API
- **Endpoints for Workouts**: The application provides API endpoints to list, create, and retrieve workout details, enabling integration with front-end frameworks or mobile apps.
- **Serializer for Workouts**: The WorkoutSerializer converts workout data to and from JSON format, facilitating easy communication with front-end components.

### User-Friendly Interface
- The application features a user-friendly interface for registration and workout logging, enhancing the overall user experience.

### Data Management
- The Workout model is linked to the User model via a foreign key, establishing a clear relationship between users and their workouts.

## Getting Started

To get a local copy of this project up and running, follow these steps:

### Prerequisites
- Node.js
- Python
- SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/irfankahn/FitnessTracker.git

2. Navigate to the project directory:
   bash

cd fitness-tracker
Install frontend dependencies:
bash

cd frontend
npm install
Install backend dependencies:
bash

cd backend
pip install -r requirements.txt

### Usage
Start the Django backend server:
bash

cd backend
python manage.py runserver

### Start the React frontend:
bash

cd frontend
npm start
Once both servers are running, navigate to http://localhost:3000 to access the application. You can register a new account, log in, and start tracking your workouts.

### Contributing
Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.





