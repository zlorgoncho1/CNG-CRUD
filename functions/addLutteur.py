from .database import databaseConnexion
from tkinter import messagebox
from datetime import datetime
from .insertVerification import strHasOthersCaract, intHasOthersCaract, verifyCombat

def addLutteur(nom, prenom, pseudo, ecurie, date, nbr_combat, nbr_victoire, nbr_nul, container, root, switcher, clean):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	try:
		ddn = datetime.strptime(date, "%m/%d/%y").strftime('%Y-%m-%d')
		if ((nom == '') or (prenom == '') or (pseudo == '') or (ecurie == '') or (nbr_combat == '') or (nbr_victoire == '') or (nbr_nul == '')):
			messagebox.showinfo(message="Veuillez Remplir tous les champs")

		elif strHasOthersCaract(nom) or strHasOthersCaract(prenom) or strHasOthersCaract(ecurie):
			messagebox.showinfo(message="Les champs \"nom\", \"prenom\", \"ecurie\", ne doivent contenir ni de chiffres`,\nni de caracteres spéciaux !")

		elif intHasOthersCaract(nbr_combat) or intHasOthersCaract(nbr_victoire) or intHasOthersCaract(nbr_nul):
			messagebox.showinfo(message="Les champs \"nbr_combat\", \"nbr_victoire\", \"nbr_nul\", ne doivent contenir que des chiffres !")

		elif (int(nbr_combat) < 0 or int(nbr_victoire) < 0 or int(nbr_nul) < 0):
			messagebox.showinfo(message="Les champs \"nbr_combat\", \"nbr_victoire\", \"nbr_nul\", ne peuvent pas être négatifs!")

		elif verifyCombat(nbr_combat, nbr_victoire, nbr_nul):
			messagebox.showinfo(message="Le nombre de combat ne peut pas être inférieur au nombre de victoire cumulé au nombre de nul")

		else:
			mycursor.execute("SELECT * FROM lutteur WHERE pseudo=:pseudo", {"pseudo":pseudo.upper()})
			user = mycursor.fetchone()
			if user == None:
				sql = "INSERT INTO lutteur (pseudo, ecurie, nom, prenom, ddn, nbr_combat, nbr_victoire, nbr_nul) VALUES (:pseudo, :ecurie, :nom, :prenom, :ddn, :nbr_combat, :nbr_victoire, :nbr_nul)"
				val = {"pseudo":pseudo.upper(), "ecurie":ecurie.upper(),  "nom":nom.upper(), "prenom":prenom.upper(), "ddn":ddn.upper(), "nbr_combat":nbr_combat.upper(), "nbr_victoire":nbr_victoire.upper(), "nbr_nul":nbr_nul.upper()}
				mycursor.execute(sql, val)
				mydb.commit()
				messagebox.showinfo(message="Insertion validé !")
				mydb.close()
				clean()
				switcher(root, switcher, container, 'indexPage')
			else:
				messagebox.showinfo(message="Un utilisateur avec ce pseudo existe déjà dans la base de donnée")
	except TypeError:
		messagebox.showinfo(message="Veuillez Sélectionner la date de naissance")
	mydb.close()
