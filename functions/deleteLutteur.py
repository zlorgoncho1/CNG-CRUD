from .database import databaseConnexion
from tkinter import messagebox

def deleteLutteur(pseudo, root, switcher, previousContainer, clean):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	sql = "DELETE FROM lutteur WHERE pseudo=%s"
	val = (pseudo,)
	mycursor.execute(sql, val)
	mydb.commit()
	messagebox.showinfo(message="Lutteur Supprimé avec succès !")
	mydb.close()
	clean()
	switcher(root, switcher, previousContainer, 'indexPage')
