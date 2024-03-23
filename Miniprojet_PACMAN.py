²#!/usr/bin/env python
# -*- coding: utf-8 -*-
#v02
"""
Projet :Extension du parcours
Auteur : Nassim Belkacem 20211545
Date de création : ______________ 
Description : 

"""

#Modules importés
from tkinter import *
import random

# ----------------------------------------------------------------
# Variables globales
# ----------------------------------------------------------------

#Liste des agents (ID)
agents=[]
#Liste des états d'autonomie des agents (booleen)
sontAutonomes=[]

#Coordonnées initiales
coordLInit_Agent=30#Largeur Agent
coordHInit_Agent=30#Hauteur Agent

coordXInit=[]#Abscisse Agent
coordYInit=[]#Ordonnée Agent

coordXInit_1=[] #Abscisse Pièce
coordYInit_1=[] #Ordonnée Pièce

coordLInit_Pieces_1=30 #Largeur Pieces
coordHInit_Pieces_1=30 #Hauteur Pieces

#Vitesses initiales
vitX=[]
vitY=[]

VIT_MAX_Joueur = 12
VIT_MAX_Autonome = 12

#Etat de fonctionnement des agents
#Valeurs comprises entre 0 et 100 (0=HS)
etats_fonctionnement=[]
DOMMAGE=5
ETAT_FONCTIONNEMENT_MAX=100

#Dimensions
LARG_CANVAS = 760
HAUT_CANVAS = 680

#nombre d'agents HS

LARG_CASE=40#Largeur
HAUT_CASE=40#Hauteur

#Couleurs Agents
couleursAgents=[]
COULEUR_AUTO=("grey","blue","silver","purple","black","pink")
COULEUR_NON_AUTO="yellow"
COULEUR_PROBLEME="red"

#Etat des animations et déplacements
etat_actif_depl_anim = False

#Liste des pièces
pieces=[]
pieces2=[]
TAILLE_PIECE=12

#Score
score=0
VAL_PIECE=10

#Demande d'arrêt
dde_arret = False

niveau2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 0, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 0, 1, 4, 0, 4, 1, 0, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 1, 0, 1, 4, 1, 4, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 4, 1, 4, 0, 0, 0, 4, 1, 4, 1, 4, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 4, 1, 4, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 0, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 0, 1, 4, 1, 4, 1, 4, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0],
    [0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 0, 1, 4, 0, 4, 1, 0, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

niveau1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 0, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 0, 1, 4, 0, 4, 1, 0, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 1, 0, 1, 4, 1, 4, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 4, 1, 4, 0, 0, 0, 4, 1, 4, 1, 4, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 4, 1, 4, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 0, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 0, 1, 4, 1, 4, 1, 4, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0],
    [0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 0, 1, 4, 0, 4, 1, 0, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------
# Fonctions
# ----------------------------------------------------------------

        

"""
Obj: Tirage aléatoire d'un emplacement sans mur
Retour : liste de 2 élements : Coordonnées en pixel

"""
def getCoordAleatoiresSansMur():

    dispo=False
    while (not dispo):
        
        i=random.randint(0,len(niveau1)-1)
        j=random.randint(0,len(niveau1[0])-1)
        if (niveau1[i][j]==1):
            dispo=True

    return [i*LARG_CASE+5,j*HAUT_CASE+5]



"""
Obj: Convertir les indices de tableau en coordonnées pixel 
Paramètres : indices du tableau niveau
Retour : liste des 2 coordonnées en pixel 
"""
def getConvertCoordPixelenCoordNiveau(i,j):
    x=5+LARG_CASE*i
    y=5+HAUT_CASE*j
    #print(str(x)+"x"+str(y))
    return [x,y]

"""
Obj: Convertir les coordonnées pixel en indices de tableau niveau
Paramètres : coordonnées pixel
Retour : liste des 2 indices du tableau niveau1
"""
def getConvertCoordPixelenCoordNiveau(x,y):
    i=int((x-5)/(LARG_CASE-((x-5)%LARG_CASE)))
    j=int((y-5)/(HAUT_CASE-((y-5)%HAUT_CASE)))
    #print(str(i)+"x"+str(j))
    return [i,j]

"""
Obj: Controler la disponibilité d'une zone
Retour : Entier
> 0 : Mut
> 1 : Personne
"""
def getOccupCoordNiveau1(x,y):
    coordNiveau=getConvertCoordPixelenCoordNiveau(x,y)
    return niveau1[coordNiveau[0],coordNiveau[1]]



"""
Obj: Gestion des évènements du clavier

"""
def evenements(event):
    
    
    if event.keysym=="Up":
        demarrage(0,-VIT_MAX_Joueur,btnHaut,0)
    elif event.keysym=="Down":
        demarrage(0,VIT_MAX_Joueur,btnBas,0)
    elif event.keysym=="Left":
        demarrage(-VIT_MAX_Joueur,0,btnGauche,0)
    elif event.keysym=="Right":
        demarrage(VIT_MAX_Joueur,0,btnDroite,0)
    elif event.keysym=="Escape":
        arret()
    elif event.keysym=="z":
        demarrage(0,-VIT_MAX_Joueur,btnHaut,1)
    elif event.keysym=="s":
        demarrage(0,VIT_MAX_Joueur,btnBas,1)
    elif event.keysym=="q":
        demarrage(-VIT_MAX_Joueur,0,btnGauche,1)
    elif event.keysym=="d":
        demarrage(VIT_MAX_Joueur,0,btnDroite,1)
    elif event.keysym=="space":
        depart()
 
"""
Obj: Réinitialisation des couleurs des boutons

"""
def init_couleurs():
    btnDroite.config(bg="black")
    btnGauche.config(bg="black")
    btnHaut.config(bg="black")
    btnBas.config(bg="black")
    btnInit.config(bg="red")
    btnArret.config(bg="red")

 
"""
Obj: Instanciation d'un nouvel Agent
Param : true si on souhaite créer un agent autonome
"""
def creationAgent(pEstAutonome):
    global vitX,vitY,coordXInit,coordYInit,agents,sontAutonomes
    
    posInitAgent=getCoordAleatoiresSansMur()
    coordXInit.append(posInitAgent[0])
    coordYInit.append(posInitAgent[1])
    vitX.append(0)
    vitY.append(0)
    if (pEstAutonome):
        agents.append(gestionCanvas.create_arc(posInitAgent[0],posInitAgent[1],
                                        posInitAgent[0]+coordLInit_Agent,posInitAgent[1]+coordHInit_Agent,
                                        fill=COULEUR_AUTO[len(couleursAgents)],start=15,extent=330))
        couleursAgents.append(COULEUR_AUTO[len(couleursAgents)])
    else:
        agents.append(gestionCanvas.create_arc(posInitAgent[0],posInitAgent[1],
                                        posInitAgent[0]+coordLInit_Agent,posInitAgent[1]+coordHInit_Agent,
                                        fill=COULEUR_NON_AUTO,start=15,extent=330))
        couleursAgents.append(COULEUR_NON_AUTO)
    sontAutonomes.append(pEstAutonome)
    etats_fonctionnement.append(ETAT_FONCTIONNEMENT_MAX)
"""
Obj: Démarrage des déplacements du Joueur et de l'Agent autonome
Param :
    pVitesseX : Vitesse demandée par le joueur sur l'axe des abcisses
    pVitesseY : Vitesse demandée par le joueur sur l'axe des ordonnées
    pBtn : Bouton utilisé dont l'apparence doit mise à jour
"""
def demarrage(pVitesseX,pVitesseY, pBtn,pNoAgentNonAuto):
    
    #Utilisation des variables globales (non locale) >> pas de réinitialisation à chaque appel
    global dde_arret,etat_actif_depl_anim, vitX, vitY

#    for i in range(len(sontAutonomes)):
#        if not sontAutonomes[i]:
#            vitX[i]=pVitesseX
#            vitY[i]=pVitesseY
    vitX[pNoAgentNonAuto]=pVitesseX
    vitY[pNoAgentNonAuto]=pVitesseY

    
    #Couleur des boutons utilisés
    init_couleurs()
    pBtn.config(bg="blue")

    dde_arret = False
    
    if etat_actif_depl_anim == False :
        deplacements()

"""
Obj:position des pièces dans le niveau 1
"""
def creationPieces(posPiece):
    global pieces
    
    #posPiece=getCoordAleatoiresSansMur()
    
    pieces.append(gestionCanvas.create_oval(posPiece[0]+(LARG_CASE-TAILLE_PIECE)/4,
                                           posPiece[1]+(HAUT_CASE-TAILLE_PIECE)/4,
                                           posPiece[0]+TAILLE_PIECE+(LARG_CASE-TAILLE_PIECE)/4,
                                           posPiece[1]+TAILLE_PIECE+(HAUT_CASE-TAILLE_PIECE)/4,
                                           fill="yellow"))
"""
Obj:position des pièces dans le niveau 2
"""
def creationPieces2(posPiece2):
    global pieces2
    
    #posPiece=getCoordAleatoiresSansMur()
    
    pieces2.append(gestionCanvas.create_oval(posPiece2[0]+(LARG_CASE-TAILLE_PIECE)/4,
                                           posPiece2[1]+(HAUT_CASE-TAILLE_PIECE)/4,
                                           posPiece2[0]+TAILLE_PIECE+(LARG_CASE-TAILLE_PIECE)/4,
                                           posPiece2[1]+TAILLE_PIECE+(HAUT_CASE-TAILLE_PIECE)/4,
                                           fill="yellow"))

"""
Obj: Lancement de tous les déplacements
"""
def deplacements():

    global etat_actif_depl_anim, dde_arret,etats_fonctionnement
    
    i=0
    nbAgentsNonAutoHS=0
    for noAgent in range(len(agents)):
        if (etats_fonctionnement[i]>0):    #Pas de déplacement si HS
            deplacement(noAgent,sontAutonomes[i])
        else:
            nbAgentsNonAutoHS=nbAgentsNonAutoHS+1
        i+=1
        
    if nbAgentsNonAutoHS>=nbAgentNonAutonomes:#Tous agents sont HS
        dde_arret=True
        print("Echec")
        gestionCanvas.create_text(LARG_CANVAS/2,HAUT_CANVAS/2,text="Echec",font="Arial 128 italic",fill="red")

    if dde_arret == False :#Tant que le jeu ne doit pas être arrêté
        fen_princ.after(100, deplacements)#Patienter 100ms afin d'appeler à nousveau cette même fonction (récursivité)
    else:
        dde_arret = False #Arrêt pris en compte et réinitialisé
        etat_actif_depl_anim = False #Animation désactivée
        

   

"""
Obj: Gestion des déplacements de tous agents

"""
def deplacement(pNoAgent,pAutonomie):
    global agents, vitX, vitY, murs, murs2
    global etat_actif_depl_anim,score,pieces,pieces2,labelScore,labelRecord
    
    #Initialisation
    etat_actif_depl_anim = True
    mod_angle = 0


    #Récupération des coordonnées de l'agent
    coordActuelles = gestionCanvas.coords(agents[pNoAgent])

    #Liste des éléments présents dans la zone devant le Joueur (anticipation en fonction de la direction de la vitesse)
    liste_obstacles = gestionCanvas.find_overlapping(coordActuelles[0]+vitX[pNoAgent],coordActuelles[1]+vitY[pNoAgent],
                                                     coordActuelles[2]+vitX[pNoAgent],coordActuelles[3]+vitY[pNoAgent])
    collisionPorte = False # Vrai si le joueur s'apprete à entrer en collision avec une porte du niveau 1
    collisionPorte2 = False #Vrai si le joueur s'apprete à entrer en collision avec une porte du niveau 2
    collisionAutonome = False #Vrai si le joueur s'apprete à entrer en collision avec un agent autonome
    collisionMur = False #Vrai si le joueur s'apprete à entrer en collision avec un mur
    collisionPiece= False #Vrai si le joueur s'apprete à entrer en collision avec une pièce du niveau 2
    collisionPiece2= False # si le joueur s'apprete à entrer en collision avec une pièce du niveau 2
    
    if len(liste_obstacles) > 0 :#Détection de l'obstacle

        for obs in liste_obstacles : #Parcours de la liste des entités présentes dans la zone

            if obs != agents[pNoAgent] : #Collision du joueur avec un autre : mur ou agent autonome ?

                #Vérifier si obs est un mur
                if (not collisionMur):
                    m=0
                while ( m<len(murs) and collisionMur==False):
                    if obs == murs[m]:
                        collisionMur=True#Collision avec un mur détectée
                    else:
                        m=m+1
                #vérifier si obs est une pièce du niveau 1
                if (not collisionPiece):
                    p=0
                while ( p<len(pieces) and collisionPiece==False):
                    if obs == pieces[p]:
                        collisionPiece=True#Collision avec un mur détectée
                    else:
                        p=p+1
                #vérifier si obs est une pièce du niveau 2
                if (not collisionPiece2):
                    k=0
                while ( k<len(pieces2) and collisionPiece2==False):
                    if obs == pieces2[k]:
                        collisionPiece2=True#Collision avec un pièce détectée
                    else:
                        k=k+1
                
                #vérifier si obs est une porte
                if (not collisionPorte):
                    po=0
                while (po<len(portes) and collisionPorte==False):
                    if obs == portes[po]:
                        collisionPorte=True#Collision avec un mur détectée
                    else:
                        po=po+1
                if (collisionPorte and pAutonomie):
                    collisionPorte=False
                    collisionMur=True
                    
                if (not collisionPorte2):
                    pos=0
                while (pos<len(portes2) and collisionPorte2==False):
                    if obs == portes2[pos]:
                        collisionPorte2=True#Collision avec un mur détectée
                    else:
                        pos=pos+1
                if (collisionPorte2 and pAutonomie):
                    collisionPorte2=False
                    collisionMur=True
                
                
                if (not collisionMur)and (not collisionPiece)and (not collisionPorte)and (not collisionPorte2)and (not collisionPiece2):
                    collisionAutonome = True #Collision avec un autre détectée
                #break
                
    if collisionPorte and po==0: 
        c = 0
        u = 0
        l = 0
        while (c < len(murs)):
            gestionCanvas.delete(murs[c])#Supprime les murs du niveau 1
            c = c+1
        murs.clear() #murs
        while (u< len(pieces)):
            gestionCanvas.delete(pieces[u])#Supprime les pièces du niveau 1
            u=u+1
        pieces.clear()#pieces[]
        while (l<len(portes)):
            gestionCanvas.delete(portes[l])#Supprime les pièces du niveau 1
            l=l+1
        portes.clear()#portes[]
        for i in range(len(niveau2)):
            for j in range(len(niveau2[i])):
                if (niveau2[i][j]==0):
                    murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="cyan"))
                elif (niveau2[i][j]==5):
                    portes2.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="black"))
                    #Affichage pièces du niveau 2
                elif (niveau2[i][j]==4):
                    creationPieces2 ([i*LARG_CASE+5,j*HAUT_CASE+5])
                    print("Porte n°"+str(po))
        print("Porte n°"+str(po))
        gestionCanvas.move(agents[pNoAgent],16*LARG_CASE,0)
    if collisionPorte and po==1: 
        c = 0
        u = 0
        l = 0
        while (c < len(murs)):
            gestionCanvas.delete(murs[c]) #Supprime les murs du niveau 1
            c = c+1
        murs.clear()#murs=[]
        while (u<len(pieces)):
            gestionCanvas.delete(pieces[u]) #Supprime les pièces du niveau 1
            u=u+1
        pieces.clear()#pieces[]
        while (l<len(portes)):
            gestionCanvas.delete(portes[l]) #Supprime les portes du niveau 1
            l=l+1
        portes.clear()#portes[]
        for i in range(len(niveau2)):
            for j in range(len(niveau2[i])):
                if (niveau2[i][j]==0):
                    murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="cyan"))
                elif (niveau2[i][j]==5):
                    portes2.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="black"))
                    #Affichage pièces du niveau 2
                elif (niveau2[i][j]==4):
                    creationPieces2 ([i*LARG_CASE+5,j*HAUT_CASE+5])
                    print("Porte n°"+str(po))
        gestionCanvas.move(agents[pNoAgent],-16*LARG_CASE,0)
    if collisionPorte2 and pos==0: 
        c = 0
        u = 0
        l = 0
        while (c < len(murs2)):
            gestionCanvas.delete(murs2[c])#Supprime les murs du niveau 2
            c = c+1
        murs2.clear() #murs
        while (u< len(pieces2)):
            gestionCanvas.delete(pieces2[u])#Supprime les pièces du niveau 2 
            u=u+1
        pieces2.clear()#pieces[]
        while (l<len(portes2)):
            gestionCanvas.delete(portes2[l])#Supprime les portes du niveau 2
            l=l+1
        portes2.clear()#portes[]
        for i in range(len(niveau1)):
            for j in range(len(niveau1[i])):
                if (niveau1[i][j]==0):
                    murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="cyan"))
                elif (niveau1[i][j]==3):
                    portes.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="black"))
                    #Affichage pièces du niveau 2
                elif (niveau1[i][j]==1):
                    creationPieces ([i*LARG_CASE+5,j*HAUT_CASE+5])
                    print("Porte n°"+str(po))
        print("Porte n°"+str(po))
        gestionCanvas.move(agents[pNoAgent],16*LARG_CASE,0)
    if collisionPorte2 and pos==1: 
        c = 0
        u = 0
        l = 0
        while (c < len(murs2)):
            gestionCanvas.delete(murs2[c])#Supprime les murs du niveau 2
            c = c+1
        murs2.clear() #murs
        while (u< len(pieces2)):
            gestionCanvas.delete(pieces2[u])#Supprime les pièces du niveau 2
            u=u+1
        pieces2.clear()#pieces[]
        while (l<len(portes2)):
            gestionCanvas.delete(portes2[l])#Supprime les portes du niveau 2
            l=l+1
        portes2.clear()#portes[]
        for i in range(len(niveau1)):
            for j in range(len(niveau1[i])):
                if (niveau1[i][j]==0):
                    murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="cyan"))
                elif (niveau1[i][j]==3):
                    portes.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="black"))
                    #Affichage pièces du niveau 2
                elif (niveau1[i][j]==1):
                    creationPieces ([i*LARG_CASE+5,j*HAUT_CASE+5])
                    print("Porte n°"+str(po))
        print("Porte n°"+str(po))
        gestionCanvas.move(agents[pNoAgent],-16*LARG_CASE,0)
    
        
                

        
   
        
    
        
    if collisionAutonome == True :#Changement de la couleur de l'agent si il est en collision
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_PROBLEME)
        
        if(etats_fonctionnement[pNoAgent]<DOMMAGE):
            etats_fonctionnement[pNoAgent]=0
            vitX=[pNoAgent]=0
            vitY=[pNoAgent]=0
        etats_fonctionnement[pNoAgent]=etats_fonctionnement[pNoAgent]-DOMMAGE
        print("Agent"+str(pNoAgent)+"-"+str(etats_fonctionnement[pNoAgent])+"%")
    else:#if (pAutonomie)
        gestionCanvas.itemconfig(agents[pNoAgent], fill=couleursAgents[pNoAgent])
    #else :
     #   gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_NON_AUTO)

    
    if collisionMur :#Stopper l'agent
        vitX[pNoAgent]=0
        vitY[pNoAgent]=0
    elif collisionPiece and not pAutonomie:
        gestionCanvas.delete(pieces.pop(p))
#        gestionCanvas.delete(pieces2.pop(p))
        #pieces.pop(p)
        score=score+VAL_PIECE
        labelScore.configure(text="Score:"+str(score))
#        labelRecord.configure(text="Record:"+str(record))
        print("score:"+str(score))
        if(len(pieces)==0 and len(pieces2)==0):
            print("Victoire")
            gestionCanvas.create_text(LARG_CANVAS/2,HAUT_CANVAS/2,text="Victoire",
                                      font="Arial 128 italic",fill="green")
            dde_arret=True
    elif collisionPiece2 and not pAutonomie:
        gestionCanvas.delete(pieces2.pop(k))
#        gestionCanvas.delete(pieces2.pop(p))
        #pieces.pop(p)
        score=score+VAL_PIECE
        labelScore.configure(text="Score:"+str(score))
#        labelRecord.configure(text="Record:"+str(record))
        print("score:"+str(score))
        if(len(pieces)==0 and len(pieces2)==0):
            print("Victoire")
            gestionCanvas.create_text(LARG_CANVAS/2,HAUT_CANVAS/2,text="Victoire",
                                      font="Arial 128 italic",fill="green")
            dde_arret=True

    else :    
        if (vitX[pNoAgent] <0 or vitY[pNoAgent]>0) :#Rotation de la représentation de l'agent en cas de changement de sens
            mod_angle = 180

        if (vitX[pNoAgent]!=0 or vitY[pNoAgent]!=0):
            #Affichage de l'agent en sens direction horizontale comme un cercle incomplet de 30 à 360° ou de 15 à 330°
            if vitY[pNoAgent] == 0 :
                if (gestionCanvas.itemcget(agents[pNoAgent], 'start') == '15.0' or gestionCanvas.itemcget(agents[pNoAgent], 'start') == '195.0') :
                    gestionCanvas.itemconfig(agents[pNoAgent], start=30+mod_angle, extent=300)
                else:
                    gestionCanvas.itemconfig(agents[pNoAgent], start=15+mod_angle, extent=330)

            #Affichage de l'agent en sens direction verticale comme un cercle incomplet de 120 à 300° ou de 105 à 330°
            if vitX[pNoAgent] ==0 :
                if (gestionCanvas.itemcget(agents[pNoAgent], 'start') == '105.0' or gestionCanvas.itemcget(agents[pNoAgent], 'start') == '285.0') :
                    gestionCanvas.itemconfig(agents[pNoAgent], start=120+mod_angle, extent=300)
                else:
                    gestionCanvas.itemconfig(agents[pNoAgent], start=105+mod_angle, extent=330)

            #placement de l'agent
            gestionCanvas.move(agents[pNoAgent],vitX[pNoAgent],vitY[pNoAgent])

    if (pAutonomie):

            #Tirage aléatoire d'un pourcentage de la direction
            direction = random.randint(1,100)

            if (vitX[pNoAgent]==0 and vitY[pNoAgent]==0): #Changement de direction si nous sommes à l'arrêt
                if direction <= 25 :#25% de chance qu'il parte à droite
                    vitX[pNoAgent] = VIT_MAX_Autonome
                    vitY[pNoAgent] = 0

                elif direction <= 50 :#25% de chance qu'il parte à gauche
                    vitX[pNoAgent] = -VIT_MAX_Autonome
                    vitY[pNoAgent] = 0

                elif direction <= 75 :#25% de chance qu'il parte en bas
                    vitX[pNoAgent] = 0
                    vitY[pNoAgent] = VIT_MAX_Autonome

                else:# de 75% et 100% inclus
                    vitX[pNoAgent] = 0#25% de chance qu'il parte en haut
                    vitY[pNoAgent] = -VIT_MAX_Autonome


"""
Obj: Afficher un autre niveau
"""
#collisionNiveau==False
#coordActuelles = gestionCanvas.coords(agents[pNoAgent])
#def teleportation(niveau1,niveau2,niveau3,agents):
#    canvas.coords(agent, x0, y0, x1, y1)
#    if(collisionNiveau==True):
#         canvas.delete(murs[])
#         canvas.delete(agents[])
#         canvas.delete(pieces[])
#coordActuelles = gestionCanvas.coords(agents[pNoAgent])
"""
Obj: Réinitialisation toutes les positions et les vitesses et arrêt des animations et déplacements
"""
def depart():

    global vitX, vitY,score
    
    #Mise à jour des boutons
    init_couleurs()
    btnInit.config(bg="blue")

    #Annulation de la vitesse en cours
    for i in range (len(vitX)):
        vitX[i]=0
    for i in range (len(vitY)):
        vitY[i]=0

    #Arrêt des animations et déplacement
    arret()

    #Repositionnement aux valeurs initiales
    i=0
    for a in agents:
        gestionCanvas.coords(a,coordXInit[i],coordYInit[i],
                             coordXInit[i]+coordLInit_Agent,coordYInit[i]+coordHInit_Agent)
        gestionCanvas.itemconfig(a, start=15,extent=330)
        i=i+1
        
    #Réinitialisation des états de fonctionnement
    for i in range (len(etats_fonctionnement)):
        etats_fonctionnement[i]=ETAT_FONCTIONNEMENT_MAX  
        
    #réinitialisation du score
    score=0
    labelScore.configure(text="Score:"+str(score))
    
    

"""
Obj: Arrêt des animations et déplacements sans repositionner
"""
def arret():
    global dde_arret
        
    #Mise à jour des boutons
    init_couleurs()
    btnArret.config(bg="blue")

    #Mise à jour de la variale globale utilisée dans les déplacements
    dde_arret = True

# ----------------------------------------------------------------
# Corps du programme
# ----------------------------------------------------------------

#Paramétrage de la fenêtre principale
fen_princ = Tk()
fen_princ.title("PACAGENT L1 SPI")
fen_princ.geometry("1900x1080")#Dimensions de la fenêtre
fen_princ.bind("<Key>",evenements)#Définition de la fonction de gestion des évènements clavier

#Paramétrage du Canvas
gestionCanvas = Canvas(fen_princ, width=LARG_CANVAS, height=HAUT_CANVAS, bg='black', bd=0, highlightthickness=0)
gestionCanvas.grid(row=0,column=0, padx=10,pady=10)

#Affichage pièces du niveau 1
pieces=[]
for i in range(len(niveau1)):
    for j in range(len(niveau1[i])):
        if (niveau1[i][j]==1):
            creationPieces([i*LARG_CASE+5,j*HAUT_CASE+5])
    




#Affichage des murs du niveau 1
murs=[]
murs2=[]
portes=[]
portes2=[]
for i in range(len(niveau1)):
    for j in range(len(niveau1[i])):
        if (niveau1[i][j]==0):
            murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="blue4"))
        elif (niveau1[i][j]==3):
            portes.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="black"))
#Affivhage des murs du niveau 2
        
#Affichage des agents gérés par l'utilisateur
nbAgentNonAutonomes=1
for i in range(nbAgentNonAutonomes):
    creationAgent(False)

#Affichage des agents autonomes
nbAgentAutonomes=3
for i in range(nbAgentAutonomes):
    creationAgent(True)

#Zone dédiée aux boutons
zoneBtn = Frame(fen_princ)
zoneBtn.grid(row=0,column=1,ipadx=5)

#Boutons directionnels
btnDroite = Button(zoneBtn, text=">>>", fg="yellow", bg="black", command=lambda:demarrage(VIT_MAX_Autonome,0,btnDroite,0))
btnDroite.pack(fill=X)

btnGauche = Button(zoneBtn, text="<<<", fg="yellow", bg="black", command=lambda:demarrage(-VIT_MAX_Autonome,0,btnGauche,0))
btnGauche.pack(fill=X)

btnHaut = Button(zoneBtn, text="^^^", fg="yellow", bg="black", command=lambda:demarrage(0,-VIT_MAX_Autonome,btnHaut,0))
btnHaut.pack(fill=X)

btnBas = Button(zoneBtn, text="vvv", fg="yellow", bg="black", command=lambda:demarrage(0,VIT_MAX_Autonome,btnBas,0))
btnBas.pack(fill=X)

#Boutons d'arrêt et de réinitialisation
btnArret = Button(zoneBtn, text="STOP", fg="yellow", bg="red", command=arret)
btnArret.pack(fill=X)
btnInit = Button(zoneBtn, text="INIT", fg="yellow", bg="red", command=depart)
btnInit.pack(fill=X)

#zone dédiée au score
labelScore=Label(zoneBtn,text="Score:0")
labelScore.pack()
labelRecord=Label(zoneBtn,text="Record=")
labelRecord.pack()

#Rafraichissement de la fenêtre et de tout son contenu
fen_princ.mainloop()
