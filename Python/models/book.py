# -*- coding: utf-8 -*-

"""
Classe Book
"""

# pour simplifier les annotations de types des classes non importées à l'exécution
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    """ Class representing a novel writen in French """
    isbn: int
    title: str
    summary: str
    main_characters: str
    release_date: date
    page_number: int
    author_name: str
    author_biography: str

    def __str__(self) -> str:
        result : str = ""
        result += f"Titre : {self.title}, Auteur : {self.author_name}, Résumé : \n{self.summary}, \nPersonnages : {self.main_characters}, \nDate : {self.release_date}, Pages : {self.page_number}, ISBN : {self.isbn}"
        if self.author_biography is not None:
            result += f", \nAutobiographie : {self.author_biography}"
        return result
