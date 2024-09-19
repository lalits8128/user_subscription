# SQLAlchemy Instance Is Imported
from database import db


# Declaring Model
class Subscribe(db.Model):
    __tablename__ = "Subscription"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subscription = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
