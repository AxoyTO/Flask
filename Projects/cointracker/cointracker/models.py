from cointracker import db


class Sparkline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_updated = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Sparkline graph was last updated on'{self.date_updated}"
