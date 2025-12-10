# -*- coding: utf-8 -*-

"""
Classe EditorDao[Editor] implémentant les opérations CRUD pour l'entité Editor.
"""

from daos.dao import Dao
from typing import Optional
from models.editor import Editor

import pymysql.cursors

class EditorDao(Dao[Editor]):

    def read(self, id_entity: int) -> Optional[Editor]:
        """ Renvoi l'objet Editor correspondant à l'entité dont l'id est id_entity
                  (ou None s'il n'a pu être trouvé)"""
        editor: Optional[Editor]

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM editor WHERE id=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()  # commit

        # Vérifie que le livre existe : si oui création de l'objet et récuperation des données
        if record is not None:
            editor = Editor(record['id'],
                            record['editor_name'])
        # sinon retourne None
        else:
            editor = None
        return editor

    def read_all(self) -> Optional[list[Editor]]:
        ...

    def create(self, obj: Editor) -> int:
        ...

    def update(self, obj: Editor) -> bool:
        ...

    def delete(self, obj: Editor) -> bool:
        ...
