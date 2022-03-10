from .database import databaseConnexion
from tkinter import messagebox

def connexion(usernameEntryText, passwordEntryText, previousContainer, root, switcher):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	username = usernameEntryText.get()
	password = passwordEntryText.get()
	sql = ("SELECT * FROM administration WHERE username =:username AND password =:password", {"username":username, "password":password})
	mycursor.execute("SELECT * FROM administration WHERE username =:username AND password =:password", {"username":username, "password":password})

	admin = mycursor.fetchone()
	mydb.close()
	if admin == None:
		messagebox.showinfo(message="Identifiants Incorrects")
	else:
		print("Connexion réussie en tant que", admin)
		switcher(root, switcher, previousContainer, 'indexPage')