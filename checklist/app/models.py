from app import db

class CLRelease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    qa_signoff = db.Column(db.String(120), index=True, unique=True)
    qa_signoff_date = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return self.name

    def qa_signoff(self, qa_signoff):
        self.qa_signoff = qa_signoff
        return self.qa_signoff
