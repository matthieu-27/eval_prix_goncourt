# -*- coding: utf-8 -*-

"""
Classe BookDao[Book] implémentant les opérations CRUD pour l'entité Book.
"""
from abc import ABC

from .dao import Dao
from typing import Optional
from Python.models.book import Book

import pymysql.cursors  # type: ignore

class BookDao(Dao[Book], ABC):
    def read(self, id_entity: int) -> Optional[Book]:
        """ Renvoit l'objet Book correspondant à l'entité dont l'id est id_entity
          (ou None s'il n'a pu être trouvé)"""
        book : Optional[Book]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book WHERE isbn=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()

        if record is not None:
            book = Book(record['isbn'],
                        record['title'],
                        record['summary'],
                        record['main_characters'],
                        record['release_date'],
                        record['page_number'],
                        record['author_name'],
                        record['author_biography'])
        else:
            book = None
        return book