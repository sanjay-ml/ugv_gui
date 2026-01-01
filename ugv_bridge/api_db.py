import sqlite3
from fastapi import FastAPI

app=FastAPI()

db=sqlite3.connect("ugv.db",check_same_thread=False)
cursor=db.cursor()

@app.post("/add_user")
def add_user(name: str, email: str):
    cursor.execute(
        "INSERT INTO users (name,email) VALUES (?,?)",
        (name, email)
    )
    db.commit()
    return{"added": True}

@app.get("/users")
def list_users():
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]
