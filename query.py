"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet')

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Model.query.filter(Model.year > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

Brand.query.filter( (Brand.discontinued!=None) | (Brand.founded < 1950) ).all()

# Get all models whose brand_name is not Chevrolet.

Model.query.filter(Model.name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    results = db.session.query(Model.name, 
                            Model.brand_name, 
                            Brand.headquarters).join(Brand).filter(Model.year==year).all()

    for name, brand_name, headquarters in results:
        print name, brand_name, headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    next_results = db.session.query(Model.brand_name, 
                                    Model.name).all()

    for brand_name, name in next_results:
        print brand_name, name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
#
# Brand.query.filter_by(brand_name='Ford').one() returns a Model object
# or, alternatively, a corresponding row (with populated field data)
# in the models table. 

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
# 
# An association table is like a middle table in that it serves as the 
# connection between tables that are not directly connected. It is
# merely the glue as it connects those tables. It does not contain 
# any meaningful information beyond the connections between other
# tables. An association handles many to one relationships (with
# crowsfeet pointing at the association table).


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
    return Brand.query.filter(Brand.name.like('%mystr%')).all()


def get_models_between(start_year, end_year):

    return Brand.query.filter(Brand.year.between(start_year, end_year)).all()
