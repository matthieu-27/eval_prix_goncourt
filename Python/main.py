from Python.buisness.goncourt import Goncourt

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue au Prix Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()

    book1 = goncourt.get_book_by_isbn(9782710015871)
    print(book1.__str__())