from .database import databaseConnexion
from tkinter import messagebox
from datetime import datetime

def setLutteur(nom, prenom, pseudo, ecurie, date, nbr_combat, nbr_victoire, nbr_nul, container, root, switcher, clean):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	try:
		ddn = datetime.strptime(date, "%m/%d/%y").strftime('%Y-%m-%d')
		if ((nom == '') or (prenom == '') or (pseudo == '') or (ecurie == '') or (nbr_combat == '') or (nbr_victoire == '') or (nbr_nul == '')):
			messagebox.showinfo(message="Veuillez Remplir tous les champs")
		else:
			sql = "UPDATE lutteur SET nom=%s, prenom=%s, ecurie=%s, ddn=%s, nbr_combat=%s, nbr_victoire=%s, nbr_nul=%s WHERE pseudo=%s"
			val = (nom, prenom, ecurie, ddn, nbr_combat, nbr_victoire, nbr_nul, pseudo)
			mycursor.execute(sql, val)
			mydb.commit()

			messagebox.showinfo(message="Modification Effectuée !")
			mydb.close()
			clean()
			switcher(root, switcher, container, 'indexPage')

	except TypeError:
		messagebox.showinfo(message="Veuillez Sélectionner la date de naissance")
	mydb.close()
