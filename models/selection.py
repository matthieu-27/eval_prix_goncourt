# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from __future__ import annotations
from datetime import date
from dataclasses import dataclass, field


@dataclass
class Selection:
    id: int
    selection_number: int
    vote_round: int
    selection_date: date

    def __str__(self):
        return f"Sélection {self.selection_number} du {self.selection_date} [{self.vote_round}{"er" if self.vote_round == 1 else "ème"} tour]"
