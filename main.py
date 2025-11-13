from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data CLass - Row of data
class MyTask(db.Model):
    id = db.column(db.Interger, primary_key=True)
    content = db.column(db.string(100), nullable=False)
    complete = db.column(db.Interger, default=0)
    created = db.column(db.DateTime, default=datetime.UTC)

    def __repr__(self) -> str:
        return f"Task {self.id}"



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)
