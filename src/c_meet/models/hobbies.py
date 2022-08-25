from c_meet import db
import uuid

class Hobby(db.Model):
    __tablename__ = 'hobbies'

    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    type = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, type=None):
        self.text = type
        self.created_at = db.func.now()
        self.updated_at = db.func.now()

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()

    def __repr__(self):
        return 
