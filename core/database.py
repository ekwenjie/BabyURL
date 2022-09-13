from core import db
from datetime import datetime

class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(1000), nullable=False)
    short_id = db.Column(db.String(25), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)