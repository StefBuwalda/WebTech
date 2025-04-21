
# Installation Guide

## Setting Up Your Virtual Environment

### 1. Create a Virtual Environment
To begin, create a virtual environment using the following command:
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment
For Windows, activate the virtual environment with:
```bash
.\venv\Scripts\activate.bat
```

### 3. Install Required Packages
Once the environment is activated, install the necessary packages by running:
```bash
pip install -r requirements.txt
```

---

## Setting Up the Database

### 1. Initialize the Database
To initialize the database, run the following command:
```bash
flask --app app.py db init
```

### 2. Migrate the Database
Migrate the database schema to the latest version with:
```bash
flask --app app.py db migrate
```

### 3. Upgrade the Database
Apply the migration to update the database with:
```bash
flask --app app.py db upgrade
```

---

## Seeding the Database
To populate the database with a few sample users and services, run:
```bash
python seed.py
```

---

## Starting the Application
To start the application, run:
```bash
python app.py
```

---

# Development Commands

### Updating `requirements.txt`
To update the `requirements.txt` with the currently installed packages, use the following command:
```bash
pip freeze > requirements.txt
```

---
