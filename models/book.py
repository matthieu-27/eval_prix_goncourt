# -*- coding: utf-8 -*-

"""
Classe Book
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    """Livre faisant partie du prix goncourt :
    - isbn                 : clé primaire de l'entité persistante
    - title                : titre du livre
    - summary              : sommaire
    - main_characters      : personnages principaux
    - page_number          : nombre de pages
    - author_name          : nom de l'auteur du livre
    - author_biography     : biographie optionnelle de l'auteur
    """
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
