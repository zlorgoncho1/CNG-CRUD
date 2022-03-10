from .database import databaseConnexion
from tkinter import messagebox
from datetime import datetime

def readLutteur(index, root, switcher, previousContainer, pagename):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	sql = "SELECT * FROM Lutteur WHERE pseudo=:pseudo"
	val = {"pseudo":index}
	mycursor.execute(sql, val)
	lutteur = mycursor.fetchone()
	mydb.close()
	pseudo = lutteur[0]
	ecurie = lutteur[1]
	nom = lutteur[2]
	prenom = lutteur[3]
	ddn = datetime.strptime(str(lutteur[4]), '%Y-%m-%d').strftime("%m/%d/%y")
	nbr_combat = lutteur[5]
	nbr_victoire = lutteur[6]
	nbr_nul = lutteur[7]
	switcher(root, switcher, previousContainer, pagename, pseudo=pseudo, ecurie=ecurie, nom=nom, prenom=prenom, ddn=ddn, nbr_combat=nbr_combat, nbr_victoire=nbr_victoire, nbr_nul=nbr_nul)