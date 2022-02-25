from .database import databaseConnexion
from layouts.indexPage import indexPage

def connexion(usernameEntryText, passwordEntryText, previousContainer, root):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	username = usernameEntryText.get()
	password = passwordEntryText.get()
	sql = "SELECT * FROM administration WHERE username = %s AND password = %s"
	values = (username, password)
	mycursor.execute(sql, values)

	admin = mycursor.fetchone()
	mydb.close()
	if admin == None:
		print("Identifiants Incorrect !")
	else:
		print("Connexion réussie en tant que", admin)
		previousContainer.pack_forget()
		indexPage(root)
