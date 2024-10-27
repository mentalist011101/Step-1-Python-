import json

class ContactNOTFound(Exception):

    def __init__(self, message, value):
        self.message = message
        self.value = value


class Annuaire():
    ''' Annuaire de gestion des diferrents contatcts '''

    annuaire = {}
    def __init__(self, nom='',contact='',email=''):
        self.contact = nom
        self.email = nom+'@gmail.com'
        #nom = input("Entrez votre nom")
        self.nom = nom
        #annuaireJson = json.dumps(Annuaire.annuaire, indent=4)
        # with open('annuaire.json','r') as f:
            # person = json.load(f)
            # print(person)
    def ajouter_contact(self,nom='',contact='',email=''):
        '''Ajouter un contact a l'annuaire'''
        self.nom = nom
        self.contact = contact
        self.email = email
        
        try :
            Annuaire.annuaire[self.nom]
        except KeyError:
            Annuaire.annuaire[self.nom] = (self.contact, self.email)
            print(f'Le contact {self.nom} a été ajouté avec succès!')
            self.enregistre_format_json(Annuaire.annuaire)
        else:
            print(f'Un  contact de ce nom {self.nom} existe deja')
            conf = input('Voulez vous le modifier? tapez "y" ou le supprimer("d) ')
            if conf.lower() == 'y':
                self.mettre_a_jour(self.nom, contact, email)
            elif conf.lower() == 'd':
                self.supprimer_contact(self.nom)
        #finally:
            #print(f'un contact au nom de {self.nom} existe deja')
        

    def rechercher_contact(self,nom):
        '''Recherher un contact dans l'annuaire'''
        self.nom = nom
        if self.nom in Annuaire.annuaire:
            return f'Le numero du {self.nom} est {Annuaire.annuaire[self.nom][0]} et le mail {Annuaire.annuaire[self.nom][1]}'
        else:
            return (f'Aucun contact au nom de {self.nom} trouve')

    def mettre_a_jour(self,nom,contact=None,email=None):
        '''Modifier un contact de l'annuaire'''
        self.nom = nom
        try:
            c,e = Annuaire.annuaire[self.nom]
        except KeyError:
            print(f'Aucun contact au nom de {self.nom}')
        else:
            if contact!=None:
                self.contact = contact
                Annuaire.annuaire[self.nom] = (self.contact, e)
                print('Les modifications ont été effectuees')
                self.enregistre_format_json(Annuaire.annuaire)
            if email!=None:
                self.email = email
                Annuaire.annuaire[self.nom] = (c, self.email)
                print('Les modifications ont été effectuees')
                self.enregistre_format_json(Annuaire.annuaire)
            if email!=None and contact!=None:
                Annuaire.annuaire[self.nom] = (self.contact, self.email)
                print('Les modifications ont été effectuees')
                self.enregistre_format_json(Annuaire.annuaire)

    def supprimer_contact(self, nom):
        '''Supprimer un contact de l'annuaire'''
        self.nom = nom
        try:
            a=Annuaire.annuaire[self.nom]
        except KeyError:
            print(f"Le contact que vous voulez supprimer n'existe pas {self.nom}")
        else:
            confiramation = input("Voulez vous vraiment supprimer ce contact? tapez 'y")
            if confiramation=='y':
                del Annuaire.annuaire[self.nom]
                print(f'Le contact {self.nom} a été supprimé')
                self.enregistre_format_json(Annuaire.annuaire)
            else:
                pass

    def afficher_annuaire(self):
         print(f'NOM----------------- CONTACT -----------------MAIL')
         for key,value in Annuaire.annuaire.items():
             print(f'{key}---------------{value[0]}---------------{value[1]}')

        #print(Annuaire.annuaire)
    def enregistre_format_json(self,annuaire):
        self.annuaire=annuaire
        json_annuaire = json.dumps(annuaire, indent=4)
        with open('annuaire.json','wt') as f:
            f.write(json_annuaire)

if __name__=='__main__':
    mon_annuaire = Annuaire()

    ## Test d'utilisation

    # mon_annuaire.ajouter_contact("Luciano", contact='620693380' ,email='luci@gmail.com')
    # mon_annuaire.mettre_a_jour("Luciano", email='toto@gmail.com')
    # mon_annuaire.supprimer_contact("Luciano")
    # print(mon_annuaire.rechercher_contact("Luciano"))
    # mon_annuaire.afficher_annuaire()