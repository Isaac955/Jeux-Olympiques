# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:58:01 2021

@author: Isaac
"""
#Jeux Olympiques
from tkinter import *

# définition des fonctions gestionnaires d'événements :
def anneau1(x1, y1, x2, y2, coul):
    can1.create_oval(x1, y1, x2, y2, width=8, outline=coul)

def anneau2(x1, y1, x2, y2, coul):
    can1.create_oval(x1, y1, x2, y2, width=8, outline=coul)

def anneau3(x1, y1, x2, y2, coul):
    can1.create_oval(x1, y1, x2, y2, width=8, outline=coul)

def anneau4(x1, y1, x2, y2, coul):
    can1.create_oval(x1, y1, x2, y2, width=8, outline=coul)

def anneau5(x1, y1, x2, y2, coul):
    can1.create_oval(x1, y1, x2, y2, width=8, outline=coul)

# création du widget principal ("maître") :
fen1 = Tk()

# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='white', height=500, width=1000)
can1.pack(side=LEFT)

bou1 = Button(fen1, text='Anneau bleu', command=lambda: anneau1(40, 60, 240, 260, "blue"))
bou1.pack()

bou2 = Button(fen1, text='Anneau jaune', command=lambda: anneau2(140, 160, 340, 360, "yellow"))
bou2.pack()

bou3 = Button(fen1, text='Anneau noir', command=lambda: anneau3(240, 60, 440, 260, "black"))
bou3.pack()

bou4 = Button(fen1, text='Anneau vert', command=lambda: anneau4(340, 160, 540, 360, "green"))
bou4.pack()

bou5 = Button(fen1, text='Anneau rouge', command=lambda: anneau5(440, 60, 640, 260, "red"))
bou5.pack()

bou6 = Button(fen1, text='Quitter', command=fen1.quit)
bou6.pack(side=BOTTOM)

fen1.mainloop()  # démarrage du réceptionnaire d'événements
