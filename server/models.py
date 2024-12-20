# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin
from config import db


class Landlord(db.Model):

    __tablename__ = 'landlords_table'

    id = db.Column(db.Integer, primary_key=True)
    associated_llcs = db.Column(db.String, nullable=False)
    violations = db.Column(db.String)
    currently_in_litigation = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "associated_llcs": self.associated_llcs,
            "violations": self.violations,
            "currently_in_litigation": self.currently_in_litigation
        }