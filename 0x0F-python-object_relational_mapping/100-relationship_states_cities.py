#!/usr/bin/python3
"""list all States from the database hbtn_0e_6_usa"""


def main():
    """connect to db, read data and display as expected using ORM"""
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    san_francisco = City(name='San Francisco')
    california = State(name='California')
    california.cities.append(san_francisco)
    session.add_all([california, san_francisco])

    session.commit()
    session.flush()
    session.close()


if __name__ == '__main__':
    """execute the main function"""
    main()
