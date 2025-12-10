# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass

from daos.book_dao import BookDao
from daos.selection_dao import SelectionDao


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

    @staticmethod
    def get_selection_jury(selection_id: int):
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.get_selection_jury(selection_id)

    @staticmethod
    def get_selection(selection_id: int):
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read(selection_id)

    @staticmethod
    def get_selection_books(selection_id: int):
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.get_selection_books(selection_id)

