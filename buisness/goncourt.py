# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass

from daos.book_dao import BookDao
from daos.personality_dao import PersonalityDao


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
        personality_dao: PersonalityDao = PersonalityDao()
        return personality_dao.get_selection_jury(selection_id)
