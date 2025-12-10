# -*- coding: utf-8 -*-

"""
Classe PersonalityDao[Personality] implémentant les opérations CRUD pour l'entité Personality.
"""

from daos.dao import Dao
from typing import Optional
from models.personality import Personality

import pymysql.cursors

class PersonalityDao(Dao[Personality]):

    def read(self, id_entity: int) -> Optional[Personality]:
        """ Renvoi l'objet Personality correspondant à l'entité dont l'id est id_entity
                  (ou None s'il n'a pu être trouvé)"""
        personality: Optional[Personality]

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM personality WHERE id=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()  # commit

        # Vérifie que le livre existe : si oui création de l'objet et récuperation des données
        if record is not None:
            personality = Personality(record['id'],
                                      record['name'],
                                      record['is_president'])
        # sinon retourne None
        else:
            personality = None
        return personality

    def read_all(self) -> Optional[list[Personality]]:
        ...

    def create(self, obj: Personality) -> int:
        ...

    def update(self, obj: Personality) -> bool:
        ...

    def delete(self, obj: Personality) -> bool:
        ...

    @staticmethod
    def get_selection_jury(selection_id: int) -> Optional[list[Personality]]:
        jury: Optional[list[Personality]] = []

        with Dao.connection.cursor() as cursor:
            sql = """SELECT * FROM personality p \
                     INNER JOIN jury j \
                     ON p.id = j.personality_id \
                     WHERE j.selection_id=%s"""
            cursor.execute(sql, (selection_id,))
            records = cursor.fetchall()  # commit

        if records is not None:
            for record in records:
                personality = Personality(record['id'],
                                          record['name'],
                                          record['is_president'])
                jury.append(personality)
        else:
            jury = None
        return jury
