# os is a built is a package to perform os related activities
import os
import psycopg2
# Flask - create the application instance
# request - Make api calls, read the request info like query parameters, payload,headers
from flask import Flask, request, jsonify
# Flask_restful helps for application routing
from flask_restful import Api
# SQLAlchemy - ORM tool for postgres
# ORM - Maps Python Data to Postgrest table objects
# create_engine - Creates an engine object for database
# Column - Type for specifying the column of a database
from sqlalchemy import create_engine, Column, String, Integer,Float, Date, Boolean, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import MetaData
from dataclasses import asdict

# Flask and Flask-RESTful Setup
app = Flask(__name__)
api = Api(app)

# SQLAlchemy Setup
Base = declarative_base()
# postgresql - Adapter for interacting with database
database_url = "postgresql://postgres:1234@localhost:5432/postgres"

# Create engine with NullPool to disable connection pooling
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

class UserInfo(Base):
    __tablename__ = "user_info"
    EmployeeID = Column("emp_id", Integer, primary_key=True)
    Age = Column("age", Integer)
    Name = Column("name", String)
    Exp = Column("exp", Float)
    Gender = Column("gender", String)
    Dept = Column("dept", String)
    Country = Column("coountry", String)

metadata.create_all(engine)

@app.route('/get-records', methods = ["GET"])
def fet_records():
    if len(request.args) == 0:
        result = session.query(UserInfo).all()
        return str(result)

    if 'dept' in request.args():
        dept = request.args.get("dept")
        result = session.query(UserInfo) .filter(UserInfo.Dept == dept). all()
        return str(result)


    if 'name' in request.args():
        name = request.args.get("dept")
        result = session.query(UserInfo) .filter(UserInfo.Name == name). all()
        return str(result)


    if 'age' in request.args():
        age = request.args.get("age")
        result = session.query(UserInfo) .filter(UserInfo.Age==age). all()
        return str(result)


    if 'emp_id' in request.args():
        emp_id = request.args.get("age")
        result = session.query(UserInfo) .filter(UserInfo.EmployeeID==emp_id). all()
        return str(result)

app.run(debug=True)