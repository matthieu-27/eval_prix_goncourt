# -*- coding: utf-8 -*-

"""
Classe BookDao[Book] implémentant les opérations CRUD pour l'entité Book.
"""

from daos.dao import Dao
from typing import Optional
from models.book import Book

import pymysql.cursors  # type: ignore

class BookDao(Dao[Book]):
    def read(self, id_entity: int) -> Optional[Book]:
        """ Renvoit l'objet Book correspondant à l'entité dont l'id est id_entity
          (ou None s'il n'a pu être trouvé)"""
        book : Optional[Book]

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE isbn=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone() # commit

        # Vérifie que le livre existe : si oui création de l'objet et récuperation des données
        if record is not None:
            book = Book(record['isbn'],
                        record['title'],
                        record['summary'],
                        record['main_characters'],
                        record['release_date'],
                        record['page_number'],
                        record['author_name'],
                        record['author_biography'])
        # sinon retourne None
        else:
            book = None
        return book

    def create(self, obj: Book) -> int:
        ...

    def update(self, obj: Book) -> bool:
        ...

    def delete(self, obj: Book) -> bool:
        ...

    def read_all(self) -> Optional[list[Book]]:
        book_list: Optional[list[Book]] = []

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book"
            cursor.execute(sql)
            records = cursor.fetchall()

        if records is not None:
            for record in records:
                book = Book(record['isbn'],
                            record['title'],
                            record['summary'],
                            record['main_characters'],
                            record['release_date'],
                            record['page_number'],
                            record['author_name'],
                            record['author_biography'])
                book_list.append(book)
        else:
            book_list = None
        return book_list
