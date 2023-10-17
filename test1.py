class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        
class Auteur:
    def __init__(self, nom):
        self.nom = nom

class Bibliotheque:
    def __init__(self):
        self.collection = []
        
    def emprunter_livre(self, livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return f"{livre.titre} a ete emprunté. "
        else:
            return "Le livre n'est pas disponible."
           
           
auteur1 = Auteur("J.K. Rowling")
livre1 = Livre("Harry Potter and the Sorcerer's stone", auteur1)

biblio = Bibliotheque()
resultat = biblio.emprunter_livre(livre1)

print(resultat)