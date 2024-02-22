#!/usr/bin/python3
"""Engine for the DB"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import User, State, City, Amenity, Place, Review


class DBStorage():
    """DB storage"""
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV'==test):
            Base.metadata.drop.all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
                objects = self.__session.query(cls).all()
        else:
            objects = []
            for cls in classes:
                objects.extend(self.__session.query(cls).all())
        result = {}
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result[key] = obj

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a new database
        session"""
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sessions)
