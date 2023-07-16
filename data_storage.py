"""This module is responsible for storing and retrieving user data."""

import sqlite3
from sqlite3 import Error

USER_SCHEMA = '''
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    name text NOT NULL,
    phone text NOT NULL,
    email text NOT NULL UNIQUE,
    password text NOT NULL
);
'''

APPOINTMENT_SCHEMA = '''
CREATE TABLE IF NOT EXISTS appointments (
    id integer PRIMARY KEY,
    user_id integer NOT NULL,
    title text NOT NULL,
    description text,
    location text,
    start text NOT NULL,
    end text NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
'''

SCHEDULE_SCHEMA = '''
CREATE TABLE IF NOT EXISTS schedules (
    id integer PRIMARY KEY,
    user_id integer NOT NULL,
    day text NOT NULL,
    start text NOT NULL,
    end text NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
'''

def create_connection():
    """Create a database connection and return the connection object."""
    conn = None
    try:
        conn = sqlite3.connect(':memory:') # create a database in RAM
        print(sqlite3.version)
    except Error as error:
        print(error)
    return conn

def create_table(conn, create_table_sql):
    """Create a table in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as error:
        print(error)

def create_user(conn, user):
    """Insert a new user into the users table."""
    sql = ''' INSERT INTO users(name,phone,email,password)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid
