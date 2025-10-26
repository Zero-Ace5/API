import json
import os
from models import Book

DATA_FILE = "data.json"


def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        data = json.load(f)
    return [Book.from_dict(b) for b in data]


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump([b.to_dict() for b in books], f, indent=4)


def add_book(title, author):
    books = load_books()
    books.append(Book(title, author))
    save_books(books)


def list_books():
    for idx, book in enumerate(load_books(), 1):
        print(f"{idx}. {book}")


def issue_book(index):
    books = load_books()
    try:
        books[index-1].issue()
        save_books(books)
    except IndexError:
        print("Invalid Book ID")


def return_book(index):
    books = load_books()
    try:
        books[index-1].return_book()
        save_books(books)
    except IndexError:
        print("Invalid Book ID")


if __name__ == "__main__":
    add_book("1984", "George Orwell")
    add_book("The Alchemist", "Paulo Coelho")
    list_books()
    issue_book(1)
    print("\nAfter issuing:\n")
    list_books()
