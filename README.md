### How to install

## Setting up your virtual environment

# Creating virtual environment
python -m venv venv

# Activating environment for package installation (windows)
.\venv\Scripts\activate.bat

# Installing required packages
pip install -r requirements.txt

## Setting up the database

# Initialize database
flask --app app.py db init

# Migrate database
flask --app app.py db migrate

# upgrade database
flask --app app.py db upgrade

### Development commands
# Updating requirements.txt
pip freeze > requirements.txt