from api.models import db

class Bike(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(120))

    def __rep__(self):
        return self.make