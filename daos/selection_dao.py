# -*- coding: utf-8 -*-

"""
Classe SelectionDao[Selection] implémentant les opérations CRUD pour l'entité Selection.
"""

from daos.dao import Dao
from typing import Optional
from models.selection import Selection
from models.book import Book
import pymysql.cursors

class SelectionDao(Dao[Selection]):

    def read(self, id_entity: int) -> Optional[Selection]:
        """ Renvoi l'objet Selection correspondant à l'entité dont l'id est id_entity
                    (ou None s'il n'a pu être trouvé)"""
        selection: Optional[Selection]

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM selection WHERE id=%s"
            cursor.execute(sql, (id_entity,))
            record = cursor.fetchone()  # commit

        # Vérifie que la selection existe : si oui création de l'objet et récuperation des données
        if record is not None:
            selection = Selection(record['id'],
                                  record['selection_number'],
                                  record['vote_round'],
                                  record['selection_date'],
                                  [])
        # sinon retourne None
        else:
            selection = None
        return selection

    @staticmethod
    def get_selection_books(id_entity: int) -> Optional[list[Book]]:
        """ Récupère les livres d'une sélection.
                (ou None s'il n'a pu être trouvé)"""
        book_list: Optional[list[Book]] = []

        # début de la transaction
        with Dao.connection.cursor() as cursor:
            sql = """SELECT *
                     FROM selection_books sb
                     INNER JOIN book b ON b.isbn = sb.book_isbn 
                     WHERE sb.selection_id = %s"""
            cursor.execute(sql, (id_entity,))
            records = cursor.fetchall()  # commit

        # Vérifie que le livre existe : si oui création de l'objet et récuperation des données
        if records is not None:
            for record in records:
                book = Book(record['book_isbn'],
                            record['title'],
                            record['summary'],
                            record['main_characters'],
                            record['release_date'],
                            record['page_number'],
                            record['author_name'],
                            record['author_biography'])
                book_list.append(book)
        # sinon retourne None
        else:
            book_list = None
        return book_list

    def read_all(self) -> Optional[list[Selection]]:
        ...

    def create(self, obj: Selection) -> int:
        ...

    def update(self, obj: Selection) -> bool:
        ...

    def delete(self, obj: Selection) -> bool:
        ...

    @staticmethod
    def update_selection(selection_id: int, isbn_list: list[int]) -> bool:
        """
        Met à jour une sélection (2ème ou 3ème tour).

        Args:
            selection_id: 2 ou 3.
            isbn_list: Liste des ISBN des livres à ajouter.

        Returns:
            bool: True si succès, False sinon.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """DELETE FROM selection_books sb 
                         WHERE selection.id = %s"""
                cursor.execute(sql, (selection_id,))

            # 2. Ajouter les nouveaux livres
            for isbn in isbn_list:
                query = "INSERT INTO selection (selection_id, isbn) VALUES (%s, %s);"
                cursor.execute(query,(selection_id, isbn_list))

            Dao.connection.commit()
            return True
        except Exception as e:
            Dao.connection.rollback()
            print(f"Erreur lors de la mise à jour de la sélection: {str(e)}")
            return False
