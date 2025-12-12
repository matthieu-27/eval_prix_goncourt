# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from daos.selection_dao import SelectionDao

if TYPE_CHECKING:
    from models.book import Book
    from daos.book_dao import BookDao
    from daos.personality_dao import PersonalityDao


@dataclass
class Goncourt:
    @staticmethod
    def get_book_by_isbn(isbn: int):
        book_dao: BookDao = BookDao()
        return book_dao.read(isbn)

    @staticmethod
    def get_all_books() -> Optional[list[Book]]:
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    @staticmethod
    def get_selection_jury(selection_id: int):
        personality_dao: PersonalityDao = PersonalityDao()
        return personality_dao.get_selection_jury(selection_id)

    @staticmethod
    def get_selection(selection_id: int):
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read(selection_id)

    @staticmethod
    def update_selection(selection_id: int, isbn_list: list[int]) -> bool:
        """
        Met à jour une sélection (2ème ou 3ème tour).
        """
        # 1. Vérifier que la sélection est valide (2 ou 3)
        if selection_id not in [2, 3]:
            raise ValueError("Le numéro de sélection doit être 2 ou 3.")

        # 2. Vérifier que la sélection précédente existe
        previous_selection_id = selection_id - 1
        previous_books = Goncourt.get_selection_books(previous_selection_id)
        if not previous_books:
            raise ValueError(f"La sélection {previous_selection_id} n'existe pas.")

        # 3. Vérifier le nombre de livres
        expected_count = 8 if selection_id == 2 else 4
        if len(isbn_list) != expected_count:
            raise ValueError(f"La sélection {selection_id} doit contenir {expected_count} livres.")

        # 4. Vérifier que les livres font partie de la sélection précédente
        previous_isbns = {book.isbn for book in previous_books}
        for isbn in isbn_list:
            if isbn not in previous_isbns:
                raise ValueError(f"Le livre {isbn} ne fait pas partie de la sélection {previous_selection_id}.")

        return SelectionDao.update_selection(selection_id, isbn_list)

    @staticmethod
    def get_selection_books(selection_id: int) -> list[Book]:
        """
        Récupère les livres d'une sélection.
        """
        return SelectionDao.get_selection_books(selection_id)

    @staticmethod
    def record_random_votes() -> bool:
        """
        Enregistre des votes aléatoires pour la 3ème sélection.
        """
        return SelectionDao.record_random_votes()

    @staticmethod
    def get_winner() -> Optional[Book]:
        """
        Retourne le livre gagnant.
        Returns:
            Optional[Book]: Objet Book du livre gagnant ou None
        """
        return SelectionDao.get_winner()
