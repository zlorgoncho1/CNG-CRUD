from .database import databaseConnexion
from tkinter import messagebox
from datetime import datetime

def addLutteur(nom, prenom, pseudo, ecurie, date, nbr_combat, nbr_victoire, nbr_nul):
	try:
		nom = nom
		prenom = prenom
		pseudo = pseudo
		ecurie = ecurie
		ddn = datetime.strptime(date, "%m/%d/%y").strftime('%Y-%m-%d')
		nbr_combat = nbr_combat
		nbr_victoire = nbr_victoire
		nbr_nul = nbr_nul
		if ((nom == '') or (prenom == '') or (pseudo == '') or (ecurie == '') or (nbr_combat == '') or (nbr_victoire == '') or (nbr_nul == '')):
			messagebox.showinfo(message="Veuillez Remplir tous les champs")
		else:
			mydb = databaseConnexion()
			mycursor = mydb.cursor()

			sql = "INSERT INTO lutteur (pseudo, ecurie, nom, prenom, ddn, nbr_combat, nbr_victoire, nbr_nul) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			val = (pseudo, ecurie, nom, prenom, ddn, nbr_combat, nbr_victoire, nbr_nul)
			mycursor.execute(sql, val)
			mydb.commit()

			messagebox.showinfo(message="Insertion validé !")
			mydb.close()

	except TypeError:
		messagebox.showinfo(message="Veuillez Sélectionner la date de naissance")
		mydb.close()
