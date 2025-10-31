import json
from turtledemo.nim import Nim

from pymysql.constants.FLAG import UNIQUE

from saleapp import db,app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from  sqlalchemy.orm import  relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    products = relationship('Product' ,backref="category" ,lazy=True)
    def __str__(self):
            return self.name
class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    price = Column(Float, default=0.0)
    image = Column(String(500), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)
if __name__=="__main__":
    with app.app_context():
        db.create_all()
        c1 = Category(name ="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")
        db.session.add_all([c1,c2,c3])

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                db.session.add(Product(**p))
            db.session.commit()

