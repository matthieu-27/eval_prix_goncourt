# -*- coding: utf-8 -*-

"""
Classe Personality
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Personality:
    """Personnalité étant membre du jury du prix goncourt :
    - id                   : clé primaire de l'entité persistante
    - name                 : nom de la personnalité
    - is_president         : indique le président
    """
    id: int
    name: str
    is_president: bool

    def __str__(self) -> str:
        return f"[{"Président" if self.is_president else "Membre"}] {self.name}"
