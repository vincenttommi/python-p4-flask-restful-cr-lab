from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String())
    image  = db.column(db.String())
    price  = db.column(db.Float())
    is_in_stock = db.column(db.Boolean)


def __repr__(self): 
    return  f'<plant {self.name} | In Stock:{self.is_in_stock}'

          
    
