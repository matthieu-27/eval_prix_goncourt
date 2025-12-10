# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass

from daos.book_dao import BookDao


@dataclass
class Goncourt:
    @staticmethod
    def get_book_by_isbn(isbn: int):
        book_dao: BookDao = BookDao()
        return book_dao.read(isbn)

    @staticmethod
    def get_all_books():
        book_dao: BookDao = BookDao()
        return book_dao.read_all()
