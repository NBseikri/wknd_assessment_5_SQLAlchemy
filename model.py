"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    # brand = db.relationship('Brand', backref=db.backref('models'))

    def __repr__(self):
        """Provide helpful representation for model objects when printed."""

        return "<MODEL OBJ id=%s year=%s brand_name=%s name=%s>" % (self.id, self.year, self.brand_name, self.name)

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), db.ForeignKey(Model.brand_name), nullable=True)
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    # model = db.relationship('Model', backref=db.backref('brands'))

    def __repr__(self):
        """Provide helpful representation for brand objects when printed."""

        return "<BRAND OBJ id=%s name=%s founded=%s headquarters=%s discontinued=%s>" % (self.id, self.name, self.founded, self.headquarters, self.discontinued)
# End Part 1
##############################################################################
# I'm not entirely sure what is wrong with this model.py file. I was able to 
# reach the 'Connected to DB' line when I ran it. However, I was unable to
# run queries in interactive mode. The errors I got did not point to either
# my model.py file or my query syntax. I was unable to diagnose what was wrong.
# To make sure the logic and syntax for my queries were not the issue, I created
# an alternate database with made-up seed data and corresponding model and seed files
# for three tables and ran queries that resembled the queries in this assessment. 
# I was able to see that my query logic was correct for this alternate
# test database just as a sanity check to confirm my ability to construct a model file
# and to query that database. I would like to explore what was preventing me
# from runnning queries with my advisor. In any case, I did provide queries
# for each of the prompts in the query.py file without having the benefit of 
# confirming them in interactive mode. 
##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars3'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
