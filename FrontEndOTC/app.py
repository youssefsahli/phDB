from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from flask import Flask, render_template

app = Flask(__name__)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'Products'

    ID = Column(Integer, primary_key=True)
    DCI = Column(Integer, ForeignKey('DCIs.ID'))
    Commercial = Column(String)
    Photo = Column(LargeBinary)
    TheraClass = Column(Integer, ForeignKey('TheraClass.ID')) 
    Forme = Column(String)
    Dosage = Column(String)
    Posology = Column(String)

DATABASE_URL = "sqlite:///OTC.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

@app.route("/")
def index():
    # Fetch products from the database
    session = SessionLocal()
    products = session.query(Product.Commercial).all()
    session.close()

    # Render them in a template
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)

