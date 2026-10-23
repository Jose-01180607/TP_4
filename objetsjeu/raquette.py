import tkinter as tk
from objetsjeu.briques import GestionBriques

class Raquette:
    # Caractéristiques de la raquette
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.update()
        self.raq = canvas.create_rectangle(310, 500, 440, 525, fill="blue")
        # Vitesse augmentée à 30 pour régler le temps de latence
        self.vitesse = 30 
        

    def gauche(self, event):
        # Déplace la raquette vers la gauche si elle n'est pas déjà au bord gauche du Canvas
        x1, y1, x2, y2 = self.canvas.coords(self.raq)
        if x1 > 0:
            self.canvas.move(self.raq, -self.vitesse, 0)


    def droite(self, event):
        # Déplace la raquette vers la droite si elle n'est pas déjà au bord droit du Canvas
        x1, y1, x2, y2 = self.canvas.coords(self.raq)
        largeur = self.canvas.winfo_width()
        if x2 < largeur:
            self.canvas.move(self.raq, self.vitesse, 0)

       