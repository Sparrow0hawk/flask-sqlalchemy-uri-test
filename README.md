# Testing Flask-SQLAchemy with SQLite URI

I want to use SQLite in a Flask App that uses the Flask-SQLAlchemy package.
For simplicity, I want to use an in-memory SQLite database that uses a URI filename `file::memory:`.

If we use the URI `sqlite:///file::memory:?uri=true` Flask-SQLAlchemy still creates a local file called :memory: for the database.

## Steps to reproduce

To use this repository you will need:
- Python 3.12

1. Set up a virtual environment and install dependencies
   ```bash
   python3 -m --prompt . .venv
   
   . .venv/bin/activate
   
   pip install -r requirements.txt
   ```
2. Run flask app
   ```bash
   flask run --debug
   ```
3. Check for `instance/:memory:` file
