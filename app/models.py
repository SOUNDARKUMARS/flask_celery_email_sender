from app import db

class NewsLetterEmail(db.Model):
    __tablename__='newsletter_emails'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True, nullable=False)

    def __repr__(self):
        return f"<Email {self.email}>"