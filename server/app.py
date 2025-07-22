from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Bakeries API!"})

@app.route("/bakeries", methods=["GET"])
def get_bakeries():
    bakeries = Bakery.query.all()
    return jsonify([bakery.to_dict() for bakery in bakeries])

@app.route("/bakeries/<int:id>", methods=["GET"])
def get_bakery_by_id(id):
    bakery = Bakery.query.get_or_404(id)
    return jsonify(bakery.to_dict_with_goods())

@app.route("/baked_goods/by_price", methods=["GET"])
def get_baked_goods_by_price():
    goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([good.to_dict(include_bakery=True) for good in goods])

@app.route("/baked_goods/most_expensive", methods=["GET"])
def get_most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    return jsonify(most_expensive.to_dict(include_bakery=True))

if __name__ == "__main__":
    app.run(port=5555, debug=True)
