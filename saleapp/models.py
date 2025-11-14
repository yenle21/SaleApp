import json
from base64 import encode
from turtledemo.nim import Nim
from datetime import  datetime
from enum import  Enum as RoleEnum
from pymysql.constants.FLAG import UNIQUE
from saleapp import db,app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean,Enum,DateTime
from  sqlalchemy.orm import  relationship
from flask_login import UserMixin

class UserRole(RoleEnum):
    USER =1
    ADMIN =2

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.name

class User(Base , UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password =Column(String(150), nullable=False)
    avatar = Column(String(500), default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5yTxBxqX7UPLILheEuZbgOuYver2PQLQxuQ&s")
    user_role= Column(Enum(UserRole), default=UserRole.USER)

class Category(Base):

    products = relationship('Product' ,backref="category" ,lazy=True)

class Product(Base):
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

        import hashlib
        password = hashlib.md5("123".encode("utf-8")).hexdigest()
        u1  = User(name="User", username = "user", password = password)
        db.session.add(u1)

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                db.session.add(Product(**p))
            db.session.commit()

