from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///file::memory:?uri=true"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return "<h1>Hello world</h1>"
