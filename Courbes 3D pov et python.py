

# Créé par Nous, le 28/08/2016 en Python 3.2
##### Programme principal : ############
from tkinter import *
import math
import os
from xml.dom import minidom


def initialise():
    return ""

def calcul():
    #macro M(tt) // courbe paramètrique de période 2pi
##  <3*cos(tt)+5*cos(3*tt),
##   3*sin(tt)+5*sin(3*tt),
##   sin(5*tt/2)  *sin(3*tt)+sin(4*tt)-sin(6*tt)
##  >
    nomf="formule_de_M.pov"

    f = open(nomf,'w')
    f.write("<3*cos(tt)+5*cos(3*tt),   3*sin(tt)+5*sin(3*tt),   sin(5*tt/2)  *sin(3*tt)+sin(4*tt)-sin(6*tt)  >")
    f.close()
##    a=chr(92)
##    c='"C:'+a+'Program Files'+a+'POV-Ray'+a+'v3.7'+a+'bin'+a+'pvengine" +I"Courbe parametrique Noeud.pov"  +O"rendu2.png" /exit'
#OK    os.system('"C:\Program Files\POV-Ray\v3.7\bin\pvengine" +"I"+"Courbe parametrique Noeud.pov"  +"O"+"rendu1.png" /exit')
##    a="C:\Program Files\POV-Ray\v3.7\bin\pvengine" +"I"+"Courbe parametrique Noeud.pov"  +"O"+"rendu1.png" /exit
##    print(a)
 #   if (os.system('call lancepvengine.bat "Courbe parametrique Noeud"'))==0:
    if (os.system('call lancepvengine0p.bat'))==0:
        print("OK")
        imag=can.create_image(0, 0, anchor=NW, image=PhotoImage(file="Courbe parametrique Noeud.png"))
    else:
        print("Erreur")

    print(c)
    print ("fini")

larg=600
"largeur de la fenetre à l'écran"

fen = Tk()
can = Canvas(fen, width =larg*16/9, height =larg, bg ='ivory')
##photo = PhotoImage(file="Courbe parametrique Noeud.png")
##imag=can.create_bitmap(0, 0, anchor=NW, image=PhotoImage(file="Courbe parametrique Noeud.png"))

##photo = PhotoImage(file="sortie1.gif")
##
##can.create_image(0, 0, anchor=NW, image=photo)
##can.pack()

binit = Button(fen, text ='Initialise', command =initialise)
binit.pack(side =LEFT, padx =3, pady =3)

bcalcul = Button(fen, text ='Calcul', command =calcul)
bcalcul.pack(side =LEFT, padx =3, pady =3)

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)


var = DoubleVar()
scale = Scale( fen, variable = var )
scale.pack(anchor=CENTER)

button = Button(fen, text="Récupère la valeur ", command=sel)
button.pack(anchor=CENTER)

label = Label(fen)
label.pack()

##C = Canvas(fen, bg="blue", height=384, width=512)
##coord = 10, 50, 240, 210
##arc = C.create_arc(coord, start=0, extent=150, fill="red")
##filename = PhotoImage(file = "cc.gif")
##image = C.create_image(512, 384, anchor=NE, image=filename)
##C.pack()

## Faire ALT F9 pour tester le programme
from PIL import Image, ImageTk
image = Image.open("Courbe parametrique Noeud.png")
photo = ImageTk.PhotoImage(image)

label2 = Label(fen,image=photo)
label2.image = photo
label2.pack()



mode_affichage =StringVar()  #Variable traçable par tkinter http://effbot.org/tkinterbook/variable.htm
mode_affichage.set("P")

##for text, mode in MODES:
##    b = Radiobutton(fen, text=text,
##                    variable=mode_affichage, value=mode,command=choix)
##    b.pack(side =LEFT, padx =3, pady =3)
##
##
##
##frboutons = Frame( fen)
##
##bav = Button(frboutons, text ='A', command =tournea)
##
##
##bfo.grid(row=3,column=1)
##bfom1.grid(row=3,column=2)
##bga.grid(row=3,column=4)
##bgam1.grid(row=3,column=5)
##bav.grid(row=3,column=6)
##bavm1.grid(row=3,column=7)
##bdr.grid(row=3,column=8)
##bdrm1.grid(row=3,column=9)
##
##bha.grid(row=2,column=6)
##bham1.grid(row=2,column=7)
##bba.grid(row=4,column=6)
##bbam1.grid(row=4,column=7)
##
##frboutons.pack(side=RIGHT)
##
##frboutons_composes = Frame( fen)
##bh2a2d2a2 = Button(frboutons_composes, text ='H^2A^2D^2A^2', command =tourneh2a2d2a2)
##bd2a2 = Button(frboutons_composes, text ='D^2.A^2', command =tourned2a2)
##bada = Button(frboutons_composes, text ='ADA', command =tourneada)
##bada6 = Button(frboutons_composes, text ='ADA^6', command =tourneada6)
##badb = Button(frboutons_composes, text ='ADB:10', command =tourneadb)
##bbda = Button(frboutons_composes, text ='BDA:12', command =tournebda)
##bbda4 = Button(frboutons_composes, text ='BDA^4', command =tournebda4)
##bhda= Button(frboutons_composes, text ='HDA:10', command =tournehda)
##badb5 = Button(frboutons_composes, text ='ADB^5', command =tourneadb5)
##badf = Button(frboutons_composes, text ='ADF:18', command =tourneadf)
##badf3 = Button(frboutons_composes, text ='ADF^3', command =tourneadf3)
##bhm1dm1a2 = Button(frboutons_composes, text ='H^-1.D^-1.A', command =tournehm1dm1a2)
##bhm1dm1a27 = Button(frboutons_composes, text ='(H^-1.D^-1.A)^7', command =tournehm1dm1a27)
##babam1bm1 = Button(frboutons_composes, text ='ABA-1B-1:6', command =tourneabam1bm1)
###bfo.pack(side =RIGHT, padx =3, pady =3)
##
##
##bh2a2d2a2.grid(row=1,column=1)
##bada.grid(row=1,column=2)
##bada6.grid(row=2,column=2)
##badb.grid(row=1,column=3)
##badf.grid(row=1,column=4)
##badf3.grid(row=2,column=4)
##bd2a2.grid(row=2,column=1)
##badb5.grid(row=2,column=3)
##
##bbda.grid(row=1,column=5)
##bbda4.grid(row=2,column=5)
##bhda.grid(row=1,column=6)
##babam1bm1.grid(row=1,column=7)
##
##bhm1dm1a2.grid(row=1,column=8)
##bhm1dm1a27.grid(row=2,column=8)
##
##frboutons_composes.pack(side=BOTTOM)

initialise()

fen.mainloop()

