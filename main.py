from buisness.goncourt import Goncourt
from typing import ClassVar, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.vote import Vote
    from models.selection import Selection

def display_selection(selection_id: int):
    """Affiche les livres d'une sélection (1, 2 ou 3)."""
    print(f"\n-*- Sélection {selection_id} -*-")
    books = Goncourt.get_selection_books(selection_id)
    if not books:
        print(f"Aucun livre trouvé pour la sélection {selection_id}.")
        return

    for book in books:
        print(f"- {book.title} (ISBN: {book.isbn})")
        print(f"  Auteur: {book.author_name}")
        print(f"  Résumé: {book.summary[:50]}...\n")

def update_selection():
    """Met à jour une sélection (réservé au président)."""
    while True:  # Boucle pour permettre plusieurs mises à jour
        print("\n--- Mise à jour d'une sélection (2ème ou 3ème tour) ---")

        # Demander le numéro de sélection
        try:
            selection_id = int(input("Numéro de sélection (2 ou 3, 0 pour annuler): "))
            if selection_id == 0:
                return  # Retour au menu président
            if selection_id not in [2, 3]:
                print("Numéro de sélection invalide. Veuillez entrer 2 ou 3.")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # Récupérer les livres de la sélection précédente
        previous_selection_id = selection_id - 1
        previous_books = Goncourt.get_selection_books(previous_selection_id)
        if not previous_books:
            print(f"La sélection {previous_selection_id} n'existe pas.")
            continue

        #  Demander la liste des ISBN pour la nouvelle sélection
        expected_count = 8 if selection_id == 2 else 4
        print(f"\nEntrez les ISBN des {expected_count} livres pour la sélection {selection_id} (séparés par des virgules):")

        try:
            isbn_input = input("ISBN: ")
            isbn_list = [int(isbn.strip()) for isbn in isbn_input.split(",")]

            # Mettre à jour la sélection
            try:
                success = Goncourt.update_selection(selection_id, isbn_list)
                if success:
                    print(f"Sélection {selection_id} mise à jour avec succès!")
                else:
                    print("Échec de la mise à jour de la sélection.")
            except ValueError as e:
                print(f"Erreur: {str(e)}")

        except ValueError:
            print("Erreur: Veuillez entrer des ISBN valides (nombres entiers séparés par des virgules).")

def president_menu():
    """Menu pour le président du jury."""
    while True:
        print("""
               -*- Menu Président -*-
               1. Mettre à jour une sélection (2ème ou 3ème)
               2. Enregistrer les votes (2ème sélection)
               3. Retour au menu principal
               """)
        president_choice = input("Choix: ")
        if president_choice == "1":
            update_selection()
        elif president_choice == "3":
            break
        else:
            print("Choix invalide.")


def user_menu():
    """Menu pour les utilisateurs lambda."""
    while True:
        print("""
              -*- Menu Utilisateur -*-
              1. Afficher la 1ère sélection
              2. Afficher la 2ème sélection
              3. Afficher la 3ème sélection
              4. Afficher le lauréat
              5. Retour au menu principal
              """)
        user_choice = input("Choix: ")
        if user_choice == "1":
            display_selection(1)
        elif user_choice == "2":
            display_selection(2)
        elif user_choice == "3":
            display_selection(3)
        elif user_choice == "5":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    print("""\
    --------------------------
    Bienvenue au Prix Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()

    # get by isbn
    # book1 = goncourt.get_book_by_isbn(9782710015871)
    # print(book1.__str__())

    # get all books
    # books = goncourt.get_all_books()
    # for book in books:
    #     print(book.__str__() + "\n")

    # get jury by selection id
    # jury = goncourt.get_selection_jury(1)
    # for j in jury:
    #     print(j.__str__() + "\n")

    # get selection books (Use Case 2)
    # books = goncourt.get_selection_books(1)
    # for book in books:
    #     print(book.__str__() + "\n")
    #
    # # selection test
    # selection = goncourt.get_selection(1)
    # print(selection)

    while True:
        print("""
              -*- Menu Principal -*-
              1: Menu Utilisateur
              2: Menu Présidentiel
              3: Quitter
              """)

        choice = input("Choix: ")
        if choice == "1":
            user_menu()
        elif choice == "2":
            president_menu()
        elif choice == "3":
            print("Au revoir!")
            break
        else:
            print("Choix invalide.")


