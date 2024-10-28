############ Gestion d'un annuaire téléphonique

annuaire = {}
# Définition de la classe d'exception personnalisée
class ContactExist(Exception):
    def __init__(self, message="Le contact existe déjà."):
        self.message = message
        super().__init__(self.message)

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Entrez le nom du contact à ajouter : ")
    if nom in annuaire:
        raise ContactExist(f"Le contact '{nom}' existe déjà dans l'annuaire.")
    numero = input("Entrez le numéro de téléphone du contact : ")
    email = input("Entrez l'email' du contact : ")
    annuaire[nom] = (numero, email)
    print(f"\nContact '{nom}' ajouté avec succès.")

# Fonction pour mettre à jour un contact
def mise_a_jour_contact():
    nom = input("Entrez le nom du contact à modifier : ")
    if nom not in annuaire:
        print(f"Erreur : Le contact '{nom}' n'existe pas.")
        return
    print("Laisser les champs dont vous ne voulez pas modifier vide\n")
    ancien_nom = nom
    ancien_numero, ancien_email = annuaire[nom]
    nom = input("Entrez le nouveau nom du contact: ")
    if nom in annuaire:
        raise ContactExist(f"Le contact '{nom}' existe déjà dans l'annuaire.")
    numero = input("Entrez le numéro de téléphone du contact : ")
    email = input("Entrez l'email' du contact : ")
    annuaire[ancien_nom if nom == '' else nom] = (ancien_numero if numero == '' else numero, ancien_email if email == '' else email)
    print(f"Contact '{nom}' mis à jour avec succès.")

# Fonction pour supprimer un contact
def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer : ")
    if nom not in annuaire:
        print(f"Erreur : Le contact '{nom}' n'existe pas.")
        return
    del annuaire[nom]
    print(f"Contact '{nom}' supprimé avec succès.")

# Fonction pour rechercher un contact
def rechercher_contact():
    nom = input("Entrez le nom du contact à rechercher : ")
    if nom not in annuaire:
        print(f"Erreur : Le contact '{nom}' n'existe pas.")
        return
    numero, email = annuaire[nom]
    print(f"Nom : {nom}, Numéro : {numero}, Email : {email}")

# Fonction pour afficher tout l'annuaire
def afficher_annuaire():
    if not annuaire:
        print("L'annuaire est vide.")
    else:
        for nom, (numero, email) in annuaire.items():
            print(f"Nom : {nom}, Numéro : {numero}, Email : {email}")


while True:
    print("\nMenu :")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Chercher un contact")
    print("4. Supprimer un contact")
    print("5. Afficher annuaire")
    print("6. Quitter")

    choix = input("\nChoisissez une option : ")

    if choix == "1":
        try:
            ajouter_contact()
        except ContactExist as e:
            print(e)
    elif choix == "2":
        try:
            mise_a_jour_contact()
        except ContactExist as e:
            print(e)
    elif choix == "3":
        rechercher_contact()
    elif choix == "4":
        supprimer_contact()
    elif choix == "5":
        afficher_annuaire()
    elif choix == "6":
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
