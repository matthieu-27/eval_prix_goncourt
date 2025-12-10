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

        # Vérifie que la personne existe : si oui création de l'objet et récuperation des données
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
