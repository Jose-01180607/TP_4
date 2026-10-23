from tkinter import Tk, Label, Button, Canvas, Toplevel, PhotoImage
from objetsjeu.briques import GestionBriques
from objetsjeu.balle import GestionBalle
from objetsjeu.raquette import Raquette

# creation de la fenetre d'acceuil du jeu : menu
menu = Tk()
menu.title("jeu de casse brique")
menu.geometry("800x600+400+100")
menu["bg"] = "pink"
        
# fonction permettant de lancer une partie
def lancerpartie():
    jeu = Toplevel(menu)
    jeu.title("nouvelle partie")
    jeu.geometry("800x600+400+100")
    
    # caracteristiques du canva
    largeur = 750
    hauteur = 550
    canevas = Canvas(jeu, width=largeur, height=hauteur, bg="white")
    canevas.pack(padx=5, pady=5)

    # Ajout d'une image de fond 
    image_fond = PhotoImage(file="wallpaper_casse_brique.png")
    item = canevas.create_image(0, 0, anchor='nw', image=image_fond)
    canevas.image = image_fond
    print("image de fond(item", item, ")")   

    canevas.focus_set() # indispensable pour relier les touches du clavier au code
    # bouton pour quitter la partie, zone de texte du score et de la vie  
    quitter = Button(jeu, text="QUITTER", command=jeu.destroy)
    quitter.pack(side="right",padx=15,pady=10)
    
    # bouton pour recommencer la partie
    rejouer = Button(jeu, text = "RECOMMENCER", command = lambda: [jeu.destroy(), lancerpartie()])
    rejouer.pack(side="right",padx=25, pady=10)
    
    # DECLARATION GLOBALE : Pour que le fichier de la balle puisse y accéder directement
    global points, vie
    
    points = Label(jeu, text="score: 0", font=("Helvetica", 15, "bold"))
    points.pack(side="left", padx=23, pady=5)
    
    vie = Label(jeu, text="vies: 4", font=("Helvetica", 15, "bold"))
    vie.pack(side="left", pady=5) 
    
    # appelle la classe gestionBriques dans le fichier objetsjeu.briques
    briques = GestionBriques(canevas, nb_lignes=5, nb_colonnes=10, couleur="turquoise1")
    # appelle de la classe Raquette dans le fichier objetjeu.raquette
    raquette = Raquette(canevas)
    # appelle de la classee gestionballe dans le fichier objetsjeu.balle
    balle = GestionBalle(canevas, briques=briques, raq=raquette, score=0, rayon=15, fenetre_jeu=jeu)
    
    # Liaison des touches aux méthodes de la raquette
    canevas.bind("<Left>", raquette.gauche)
    canevas.bind("<Right>", raquette.droite)

# contenu du menu : titre, bouton quitter, bouton lancer une partie
labelcb = Label(menu, text="MENU PRINCIPAL", font=("Helvetica", 20, "bold"), bg="pink")
labelcb.pack(pady=20)

boutonquitter = Button(menu, text="QUITTER", font=("Helvetica", 15), fg="red", bg="pink", command=menu.destroy)
boutonquitter.pack(side="bottom", padx=10, pady=10)

boutonpartie = Button(menu, text="Lancer partie", font=("Helvetica", 15), bg="pink", relief="flat", command=lancerpartie)
boutonpartie.pack(pady=150)

boutonrecommencer = Button(menu, text = "RECOMMENCER", font = ("Helvetica",15 ), bg ="pink", relief="flat",command = lambda: [jeu.destroy(), lancerpartie()])
boutonrecommencer.pack(pady=175)

menu.mainloop()


