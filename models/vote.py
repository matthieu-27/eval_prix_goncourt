# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Vote:
    """Représente un vote pour un livre dans une sélection."""
    selection_id: int  # 1, 2 ou 3
    book_isbn: int     # ISBN du livre
    number_of_votes: int  # Nombre de votes

    def __post_init__(self):
        if self.number_of_votes < 0:
            raise ValueError("Le nombre de votes ne peut pas être négatif.")
        if self.selection_id not in [2, 3]:
            raise ValueError("Les votes ne peuvent être enregistrés que pour les 2ème ou 3ème sélections.")
