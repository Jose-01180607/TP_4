


class GestionBriques:
    def __init__(self, canvas, nb_lignes=5, nb_colonnes=10, marge=30, espace=10, hauteur_brique=25, couleur="white"):
        self.canvas = canvas
        self.briques = []  # Liste contenant les IDs Tkinter des briques creees
        
        # Recuperation des dimensions du canvas
        self.canvas.update()  # Force la mise a jour des dimensions
        largeur_canvas = self.canvas.winfo_width()
        
        # Calcul de la largeur de chaque brique pour remplir uniformément le haut
        largeur_utile = largeur_canvas - (2 * marge) - ((nb_colonnes - 1) * espace)
        largeur_brique = largeur_utile / nb_colonnes

        # Creation des briques en grille
        for ligne in range(nb_lignes):
            for col in range(nb_colonnes):
                self.x1 = marge + col * (largeur_brique + espace)
                self.y1 = 10 + ligne * (hauteur_brique + espace)
                self.x2 = self.x1 + largeur_brique
                self.y2 = self.y1 + hauteur_brique
                
                # Dessin du rectangle sur le canvas déjà crée. Quand on voudra supprimer ou utiliser les briques on aura juste a utiliser les id dans la liste briques
                brique_id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=couleur, outline="black")
                self.briques.append(brique_id)