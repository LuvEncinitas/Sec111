import sqlite3
from flask import g
 
DATABASE_URL = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g.get_database = sqlite3.connect(DATABASE_URL)
    return db