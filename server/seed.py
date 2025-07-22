from models import db, Bakery, BakedGood
from app import app

with app.app_context():
    Bakery.query.delete()
    BakedGood.query.delete()

    b1 = Bakery(name="Delightful donuts")
    b2 = Bakery(name="Incredible crullers")

    db.session.add_all([b1, b2])
    db.session.commit()

    g1 = BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=b1.id)
    g2 = BakedGood(name="Apple-spice filled donut", price=3.5, bakery_id=b1.id)
    g3 = BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=b2.id)
    g4 = BakedGood(name="Chocolate cruller", price=100.0, bakery_id=b2.id)

    db.session.add_all([g1, g2, g3, g4])
    db.session.commit()
