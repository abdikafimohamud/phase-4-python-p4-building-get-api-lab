from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Bakery(db.Model):
    __tablename__ = "bakeries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    baked_goods = db.relationship("BakedGood", backref="bakery")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "baked_goods": [good.to_dict() for good in self.baked_goods]
        }

    def to_dict_with_goods(self):
        return self.to_dict()

class BakedGood(db.Model):
    __tablename__ = "baked_goods"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    bakery_id = db.Column(db.Integer, db.ForeignKey("bakeries.id"))

    def to_dict(self, include_bakery=False):
        data = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "bakery_id": self.bakery_id
        }

        if include_bakery:
            data["bakery"] = self.bakery.to_dict() if self.bakery else None

        return data
