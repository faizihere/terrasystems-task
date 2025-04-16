# Dynamic Site – Custom Admin Dashboard for Landing Page Content Management

This project is a Django-based web application featuring a custom admin dashboard to manage the homepage content dynamically. It includes user authentication and a styled landing page editable from a dedicated dashboard.

## Overview

- **Project Name:** `dynamic_site` (renamed from `backend`)
- **Apps:**
  - `accounts`: Handles user login, logout, and authentication logic.
  - `landing_page`: Controls homepage content, editable via the dashboard.
- **Dashboard:** A custom dashboard (`dashboard.html`) outside of Django’s default admin.

## Features

- Custom dashboard to update homepage content
- Built-in user login and logout flow
- Home page with dynamic sections populated from the database
- Migration files include initial default content

## Folder Structure

dynamic_site/ 
├── accounts/ 
│ └── migrations/ # Included to preserve default content logic 
├── landing_page/ 
│ └── migrations/ # Included to maintain initial content 
├── dynamic_site/ # Main Project
├── manage.py 
├── requirements.txt 
├── .gitignore 
└── README.md

## Setup Instructions

### 1. Clone the repo
cd dynamic_site

### 2. Set up virtual environment
python -m venv env
source env/bin/activate    # Linux/macOS
env\Scripts\activate       # Windows

### 3.  Install dependencies
pip install -r requirements.txt

### 4. Migrate the initial schema
python manage.py migrate

### 5. Run the server
python manage.py runserver