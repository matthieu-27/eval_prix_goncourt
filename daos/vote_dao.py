# -*- coding: utf-8 -*-

"""
Classe VoteDao[Vote] implémentant les opérations nécessaires pour l'entité Vote.
"""
from typing import Optional
from models.vote import Vote
from daos.dao import Dao

class VoteDao(Dao[Vote]):
    @staticmethod
    def record_votes(self, votes: list[Vote]) -> bool:
        """
        Enregistre les votes pour la 3ème sélection.
        Met à jour le champ `number_of_votes` dans `selection_books`.
        """
        try:
            with Dao.connection.cursor() as cursor:
                # Mettre à jour les votes pour chaque livre de la 3ème sélection
                for vote in votes:
                    sql = """
                        UPDATE selection_books
                        SET number_of_votes = %s
                        WHERE selection_id = %s AND book_isbn = %s;
                    """
                    cursor.execute(sql, (vote.number_of_votes, vote.selection_id, vote.book_isbn))

                Dao.connection.commit()
                return True
        except Exception as e:
            Dao.connection.rollback()
            print(f"Erreur lors de l'enregistrement des votes: {str(e)}")
            return False

    @staticmethod
    def get_votes_for_selection(self, selection_id: int) -> Optional[list[Vote]]:
        """Récupère tous les votes pour une sélection donnée."""
        votes = []
        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT selection_id, book_isbn, number_of_votes
                FROM selection_books
                WHERE selection_id = %s;
            """
            cursor.execute(sql, (selection_id,))
            records = cursor.fetchall()
            for record in records:
                votes.append(Vote(
                    selection_id=record['selection_id'],
                    book_isbn=record['book_isbn'],
                    number_of_votes=record['number_of_votes']
                ))
        return votes if votes else None

    def read(self, id_entity: int) -> Optional[Vote]:
        ...

    def read_all(self) -> Optional[list[Vote]]:
        ...

    def create(self, obj: Vote) -> int:
        ...

    def update(self, obj: Vote) -> bool:
        ...

    def delete(self, obj: Vote) -> bool:
        ...
