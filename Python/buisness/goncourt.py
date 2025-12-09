# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field

from Python.daos.book_dao import BookDao


@dataclass
class Goncourt:
    @staticmethod
    def get_book_by_isbn(isbn: int):
        book_dao: BookDao = BookDao()  # type: ignore
        return book_dao.read(isbn)