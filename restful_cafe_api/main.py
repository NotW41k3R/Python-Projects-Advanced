from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Func to convert .scalars() to dict then to ist
def list_of_dicts(cafes):
    return [cafe.to_dict() for cafe in cafes]

# API Endpoints
# Home
@app.route("/")
def home():
    return render_template("index.html")

# Random Cafe
@app.route("/random", methods=['GET'])
def random_cafe():
    count = db.session.query(Cafe).count()
    random_offset = random.randint(0, count - 1)
    random_cafe = db.session.query(Cafe).offset(random_offset).first()

    if not random_cafe:
        return jsonify(error="No cafe found"), 404
    return jsonify(cafe=random_cafe.to_dict())


# All cafes
@app.route("/all", methods=['GET'])
def all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    cafe_list = list_of_dicts(cafes)
    if not cafe_list:
        return jsonify(error="No cafe found"), 404
    return jsonify(cafes=cafe_list)


# Location Based Search
@app.route('/search', methods=['GET'])
def search_cafe():
    cafe_location= request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location==cafe_location)).scalars()
    cafe_list = list_of_dicts(cafes)
    if not cafe_list:
        return jsonify(error={"Not Found":"Sorry we have any cafes at that location."}), 404
    return jsonify(cafes=cafe_list)
    

# Add a new Cafe
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {'Success' : 'Successfully added a new Cafe'})


# Update a Coffee Price
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar_one()
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response = {'Success' : 'Successfully updated price.'})

# Delete a Cafe
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    if request.args.get('api-key') == 'TopSecretAPIKey':
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar_one_or_none()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response = {'Success' : 'Successfully deleted cafe.'})
        else:
            return jsonify({'Error' : {'Not Found': "Cafe with that ID doesn't exist"}})
    else:
        return jsonify({'Error' : {'Incorrect API': "Make sure you have the correct api_key"}})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 