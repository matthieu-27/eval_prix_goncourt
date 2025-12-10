# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from __future__ import annotations
from datetime import date
from dataclasses import dataclass, field
from typing import ClassVar, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.book import Book


@dataclass
class Selection:
    id: int
    selection_number: int
    vote_round: int
    selection_date: date
    books: Optional[list[Book]]

    def __post_init__(self):
        if self.id not in [1, 2, 3]:
            raise ValueError("Le numéro de sélection doit être 1, 2 ou 3.")
        self.books = []

    def __str__(self):
        return f"Sélection {self.selection_number} du {self.selection_date} [{self.vote_round}{"er" if self.vote_round == 1 else "ème"} tour]"
