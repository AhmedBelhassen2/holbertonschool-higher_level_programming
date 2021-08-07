#!/usr/bin/python3
""" db connection """
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    dell = session.query(State).order_by(State.id).all()
    for d in dell:
        if 'a' in d.name:
            session.delete(d)
    session.commit()
    session.close()
