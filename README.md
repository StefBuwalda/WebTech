# Updating requirements.txt
pip freeze > requirements.txt

# Creating virtual environment
python -m venv venv

# Installing required packages
pip install -r requirements.txt

# Initialize database
flask --app app.py db init

# Migrate database
flask --app app.py db migrate

# upgrade database
flask --app app.py db upgrade