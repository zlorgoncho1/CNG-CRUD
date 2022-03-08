from .database import databaseConnexion

def connexion(usernameEntryText, passwordEntryText, previousContainer, root, switcher):
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
		switcher(root, switcher, previousContainer, 'indexPage')