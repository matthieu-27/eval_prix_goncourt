# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from __future__ import annotations
from datetime import date
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import ClassVar, Optional, TYPE_CHECKING
# pour éviter une circularité des imports à l'exécution,
# les classes Student et Teacher important la classe Course
if TYPE_CHECKING:
    from models.book import Book
    from buisness.goncourt import Goncourt


@dataclass
class Selection:
    id: int
    selection_number: int
    vote_round: int
    selection_date: date
    books: Optional[list[Book]]

    def __str__(self):
        return f"Sélection {self.selection_number} du {self.selection_date} [{self.vote_round}{"er" if self.vote_round == 1 else "ème"} tour]"
