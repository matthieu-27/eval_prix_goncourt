# -*- coding: utf-8 -*-

"""
Module contenant la classe abstraite Dao<T> qui définit les opérations CRUD
pour une entité de type T.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional, Any
import pymysql.cursors  # type: ignore


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        port=3306,
                        user='goncourt',
                        password='claudel',
                        database='goncourt_award',
                        cursorclass=pymysql.cursors.DictCursor)


    @abstractmethod
    def read(self, id_entity: int) -> Optional[T]:
        """Renvoit l'objet correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        ...

