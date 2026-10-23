import math
import random
from objetsjeu.briques import GestionBriques
from objetsjeu.raquette import Raquette

class GestionBalle:
    def __init__(self, canvas, briques, raq, score=0, rayon=15, fenetre_jeu=None):
        self.canvas = canvas
        self.rayon = rayon
        self.briques = briques
        self.score = score
        self.raq = raq
        self.fenetre_jeu = fenetre_jeu
        self.vies = 4 
        
        self.canvas.update()  # Force la mise a jour des dimensions
        self.largeur_canvas = self.canvas.winfo_width()
        self.hauteur_canvas = self.canvas.winfo_height()
        
        # Si Tkinter renvoie une mauvaise dimension au démarrage, on force les vraies valeurs
        if self.largeur_canvas <= 1: self.largeur_canvas = 750
        if self.hauteur_canvas <= 1: self.hauteur_canvas = 550
        
        # Coordonnées de départ du centre de la balle 
        self.posx = (self.largeur_canvas / 2)
        self.posy = (self.hauteur_canvas * 0.75)
        
        # Création de la balle 
        self.balle = canvas.create_oval(self.posx-self.rayon, self.posy-self.rayon, self.posx+self.rayon, self.posy+self.rayon, width=1, outline='pink', fill='pink')
        
        self.vitesse = 6 
        self.angle = random.uniform(-math.pi/4, -3*math.pi/4) # Angle vers le haut
        
        self.DX = self.vitesse * math.cos(self.angle)
        self.DY = self.vitesse * math.sin(self.angle)
        
        self.deplacement() 
        
    def deplacement(self): # Fonction qui gère le déplacement et les rebonds
        if not self.canvas.winfo_exists():
            return
            
        # Rebond à droite
        if self.posx + self.rayon + self.DX > self.largeur_canvas:
            self.DX = -self.DX
                
        # Rebond à gauche
        if self.posx - self.rayon + self.DX < 0:
            self.DX = -self.DX
            
        # Rebond en haut (plafond)
        if self.posy - self.rayon + self.DY < 0:
            self.DY = -self.DY

        # VRAIE GESTION DU BAS : Perte d'une vie (uniquement si la balle descend sous la raquette)
        if self.posy + self.rayon + self.DY > self.hauteur_canvas:
            self.vies -= 1
            
            # Mise à jour graphique de l'étiquette vie du fichier principal
            import cassebrique
            cassebrique.vie.config(text=f"vies: {self.vies}")
            
            if self.vies <= 0:
                # Écrit GAME OVER au milieu de l'écran
                self.canvas.create_text(self.largeur_canvas/2, self.hauteur_canvas/2, text="GAME OVER", font=("Helvetica", 40, "bold"), fill="red")
                return # Arrête la boucle définitivement
            else:
                # Réinitialisation de la balle au centre pour la vie suivante
                self.posx = self.largeur_canvas / 2
                self.posy = self.hauteur_canvas * 0.75
                self.angle = random.uniform(-math.pi/4, -3*math.pi/4)
                self.DX = self.vitesse * math.cos(self.angle)
                self.DY = self.vitesse * math.sin(self.angle)

        # Application du déplacement
        self.posx = self.posx + self.DX
        self.posy = self.posy + self.DY
        
        self.interactionbriques()
        
        # Mise à jour des coordonnées graphiques de la balle
        self.canvas.coords(self.balle, self.posx-self.rayon, self.posy-self.rayon, self.posx+self.rayon, self.posy+self.rayon)
        
        # Fin de partie quand il n'y a plus de briques (Victoire)
        if len(self.briques.briques) == 0:
            self.canvas.create_text(self.largeur_canvas/2, self.hauteur_canvas/2, text="VICTOIRE !", font=("Helvetica", 40, "bold"), fill="green")
            return # Arrête la boucle définitivement

        # Rappel de la fonction toutes les 20 ms
        self.canvas.after(20, self.deplacement)
     
    def interactionbriques(self):
        objetstouchés = self.canvas.find_overlapping(self.posx-self.rayon, self.posy-self.rayon, self.posx+self.rayon, self.posy+self.rayon)  
        
        for objet in objetstouchés:
            # Collision avec les briques
            if objet in self.briques.briques:  
                self.canvas.delete(objet)  
                self.briques.briques.remove(objet)  
                self.score += 10 
                
                # Mise à jour graphique du score
                import cassebrique
                cassebrique.points.config(text=f"score: {self.score}")
                self.DY = -self.DY 
                break 
                
            # Collision avec la raquette
            if objet == self.raq.raq:  
                if self.DY > 0: # N'inverse que si la balle descend
                    self.DY = -self.DY
