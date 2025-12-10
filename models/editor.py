# -*- coding: utf-8 -*-

"""
Classe Editor
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Editor:
    """Livre faisant partie du prix goncourt :
    - id                   : clé primaire de l'entité persistante
    - editor_name          : éditeur du livre
    """
    id: int
    editor_name: str

    def __str__(self) -> str:
        return f"Éditeur du livre: {self.editor_name}"
