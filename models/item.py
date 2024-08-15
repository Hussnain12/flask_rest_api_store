from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description=db.Column(db.String,nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), unique=False, nullable=False)
    # when we have itemmodel object we can say obj_item.store and it will return all the items from that store
    store = db.relationship("StoreModel", back_populates="items")
    # db.relationship
    tags = db.relationship(
        "TagModel", back_populates="items", secondary="items_tags")
