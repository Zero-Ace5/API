import sqlite3
import os

DB_NAME = "notes.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
CREATE TABLE IF NOT EXISTS notes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       content TEXT NOT NULL
                       )
''')
        conn.commit()


def add_note(title, content):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notes (title, content) values(?, ?)", (title, content))
        conn.commit()


def list_notes():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content FROM notes")
        return cursor.fetchall()


def delete_note(note_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE ID=?", (note_id,))
        conn.commit()
