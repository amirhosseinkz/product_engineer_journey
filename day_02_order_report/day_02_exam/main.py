
from pathlib import Path
from reports import print_books
from readers import read_books,read_authors




BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

def main():

    books = read_books(DATA_DIR / "books.json")
    authors = read_authors(DATA_DIR / "authors.csv")

    print_books(books , authors)



if __name__ == "__main__":
    main()