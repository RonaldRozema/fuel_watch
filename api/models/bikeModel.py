from api.models import db

class Bike(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(120))
    year = db.Column(db.String(4))
    liters_in_tank = db.Column(db.Float)
    average_liter_per_100_km = db.Column(db.Float)
    manufacturer = db.Column(db.String(120))

    def __rep__(self):
        return self.make