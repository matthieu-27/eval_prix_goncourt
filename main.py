from buisness.goncourt import Goncourt

if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue au Prix Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()

    # get by isbn
    # book1 = goncourt.get_book_by_isbn(9782710015871)
    # print(book1.__str__())

    # get all books
    # books = goncourt.get_all_books()
    # for book in books:
    #     print(book.__str__() + "\n")
