import json
import os


class Book:
    def __init__(self, title, author, issued=False):
        self.title = title
        self.author = author
        self.issued = issued

    def issue(self):
        """Mark the book as issued (if not already)."""
        if not self.issued:
            self.issued = True
            print(f"Issued '{self.title}'")
        else:
            print(f"'{self.title}' is already issued.")

    def return_book(self):
        """Mark the book as returned (if it was issued)."""
        if self.issued:
            self.issued = False
            print(f"Returned '{self.title}'")
        else:
            print(f"'{self.title}' was not issued.")

    def to_dict(self):
        return {"title": self.title, "author": self.author, "issued": self.issued}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} by {self.author} ({status})"
