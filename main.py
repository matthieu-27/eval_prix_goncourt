from buisness.goncourt import Goncourt
from models.selection import Selection

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

    # get jury by selection id
    # jury = goncourt.get_selection_jury(1)
    # for j in jury:
    #     print(j.__str__() + "\n")

    # get selection books (Use Case 2)
    # books = goncourt.get_selection_books(1)
    # for book in books:
    #     print(book.__str__() + "\n")
    #
    # # selection test
    # selection = goncourt.get_selection(1)
    # print(selection)
