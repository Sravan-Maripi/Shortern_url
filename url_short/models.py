from .extensions import db
from datetime import datetime
import string
from random import choices

class Urllink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024))
    shorten_url = db.Column(db.String(6), unique=True)
    views = db.Column(db.Integer, default=0)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shorten_url = self.generate_shorten_url()
        
    def generate_shorten_url(self):
        characters = string.digits + string.ascii_letters
        shorten_url = ''.join(choices(characters, k=6))
        
        link = Urllink.query.filter_by(shorten_url=shorten_url).first()
        
        if link:
            return self.generate_shorten_url()
        return shorten_url
