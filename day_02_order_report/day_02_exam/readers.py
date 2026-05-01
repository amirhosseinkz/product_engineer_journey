import json
import csv
from pathlib import Path
from models import Book



def read_books(file_path):
    path = Path(file_path)
    books = []

    with path.open("r") as file:
        data = json.load(file)

        for book in data:
            book_obj = Book(
                id= book["id"],
                title=book["title"],
                author=book["author"],
                category=book["category"],
                price=book["price"],
                stock=book["stock"],
            )
            books.append(book_obj)

        return books





def read_authors(file_path):

    path = Path(file_path)

    authors = {}


    with path.open("r") as file:

        data = csv.DictReader(file)

        for row in data:

  

            authors[row["author"].strip()] = {

                "country": row["country"].strip()

            }


    return authors
