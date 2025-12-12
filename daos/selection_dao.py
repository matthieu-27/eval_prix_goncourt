# -*- coding: utf-8 -*-

"""
Classe SelectionDao[Selection] implémentant les opérations CRUD pour l'entité Selection.
"""
import random
from daos.dao import Dao
from typing import Optional, TYPE_CHECKING

from models.selection import Selection
from models.book import Book
from models.vote import Vote


class SelectionDao(Dao[Selection]):

    def read(self, id_entity: int) -> Optional[Selection]:
        """Renvoi l'objet Selection correspondant à l'entité
            dont l'id est id_entity (ou None s'il n'a pu être trouvé)"""
        selection: Optional[Selection]

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM selection WHERE id=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()  # commit

        # Vérifie que la selection existe :
        # si oui création de l'objet et récuperation des données
        if record is not None:
            selection = Selection(
                record["id"],
                record["selection_number"],
                record["vote_round"],
                record["selection_date"],
                [],
            )
        # sinon retourne None
        else:
            selection = None
        return selection

    @staticmethod
    def get_selection_books(selection_id: int) -> list[Book]:
        """
        Récupère les livres d'une sélection.
        """
        try:
            with Dao.connection.cursor() as cursor:
                get_books_query = """
                    SELECT b.isbn, b.title, b.summary, b.main_characters,
                        b.release_date, b.page_number, b.author_name, b.author_biography
                    FROM selection_books sb
                    JOIN book b ON sb.book_isbn = b.isbn
                    WHERE sb.selection_id = %s
                    ORDER BY b.title
                """
                cursor.execute(get_books_query, (selection_id,))
                results = cursor.fetchall()
                return [
                    Book(
                        isbn=row['isbn'],
                        title=row['title'],
                        summary=row['summary'],
                        main_characters=row['main_characters'],
                        release_date=row['release_date'],
                        page_number=row['page_number'],
                        author_name=row['author_name'],
                        author_biography=row['author_biography']
                    )
                    for row in results
                ]
        except Exception as e:
            print(f"Erreur lors de la récupération des livres: {str(e)}")
            return []

    def read_all(self) -> Optional[list[Selection]]: ...

    def create(self, obj: Selection) -> int: ...

    def update(self, obj: Selection) -> bool: ...

    def delete(self, obj: Selection) -> bool: ...

    @staticmethod
    def update_selection(selection_id: int, isbn_list: list[int]) -> bool:
        """
        Met à jour une sélection (2ème ou 3ème tour).
        """
        try:
            with Dao.connection.cursor() as cursor:
                # 1. Vérifier que tous les ISBN existent
                check_isbn_query = "SELECT isbn FROM book WHERE isbn = %s;"
                for isbn in isbn_list:
                    cursor.execute(check_isbn_query, (isbn,))
                    if not cursor.fetchone():
                        raise ValueError(f"Le livre avec ISBN {isbn} n'existe pas")

                # 2. Créer la sélection si elle n'existe pas
                check_selection_query = "SELECT id FROM selection WHERE id = %s;"
                cursor.execute(check_selection_query, (selection_id,))
                if not cursor.fetchone():
                    insert_selection_query = """
                        INSERT INTO selection (id, selection_date)
                        VALUES (%s, CURDATE())
                    """
                    cursor.execute(insert_selection_query, (selection_id,))

                # 3. Supprimer les anciens livres de la sélection
                delete_books_query = """
                    DELETE FROM selection_books
                    WHERE selection_id = %s
                """
                cursor.execute(delete_books_query, (selection_id,))

                # 4. Ajouter les nouveaux livres
                insert_books_query = """
                    INSERT INTO selection_books (selection_id, book_isbn, number_of_votes)
                    VALUES (%s, %s, 0)
                """
                params = [(selection_id, isbn) for isbn in isbn_list]
                cursor.executemany(insert_books_query, params)

            Dao.connection.commit()
            return True
        except Exception as e:
            Dao.connection.rollback()
            print(f"Erreur lors de la mise à jour de la sélection: {str(e)}")
            return False

    @staticmethod
    def record_random_votes() -> bool:
        """
        Enregistre des votes aléatoires pour la 3ème sélection.
        """
        try:
            with Dao.connection.cursor() as cursor:
                # 1. Récupérer les livres de la 3ème sélection
                get_books_query = """
                    SELECT book_isbn
                    FROM selection_books
                    WHERE selection_id = 3
                """
                cursor.execute(get_books_query)
                books = cursor.fetchall()
                if not books:
                    raise ValueError("Aucun livre trouvé pour la 3ème sélection")

                # 2. Générer des votes aléatoires (entre 1 et 10 pour chaque livre)
                votes = []
                for book in books:
                    # Créer un objet Vote pour chaque livre
                    vote = Vote(
                        selection_id=3,
                        book_isbn=book['book_isbn'],
                        number_of_votes=random.randint(1, 10)
                    )
                    votes.append(vote)

                # 3. Mettre à jour les votes
                update_votes_query = """
                    UPDATE selection_books
                    SET number_of_votes = %s
                    WHERE selection_id = 3 AND book_isbn = %s
                """
                params = [(vote.number_of_votes, vote.book_isbn) for vote in votes]
                cursor.executemany(update_votes_query, params)

            Dao.connection.commit()
            return True
        except Exception as e:
            Dao.connection.rollback()
            print(f"Erreur lors de l'enregistrement des votes: {str(e)}")
            return False

    @staticmethod
    def get_winner() -> Optional[Book]:
        """
        Retourne le livre gagnant (celui avec le plus de votes dans la 3ème sélection).
        """
        try:
            with Dao.connection.cursor() as cursor:
                get_winner_query = """
                    SELECT b.isbn, b.title, b.summary, b.main_characters,
                        b.release_date, b.page_number, b.author_name, b.author_biography
                    FROM selection_books sb
                    JOIN book b ON sb.book_isbn = b.isbn
                    WHERE sb.selection_id = 3
                    ORDER BY sb.number_of_votes DESC
                    LIMIT 1
                """
                cursor.execute(get_winner_query)
                result = cursor.fetchone()
                if result:
                    return Book(
                        isbn=result['isbn'],
                        title=result['title'],
                        summary=result['summary'],
                        main_characters=result['main_characters'],
                        release_date=result['release_date'],
                        page_number=result['page_number'],
                        author_name=result['author_name'],
                        author_biography=result['author_biography']
                    )
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération du gagnant: {str(e)}")
            return None
