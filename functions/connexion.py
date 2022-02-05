from .database import databaseConnexion

def connexion(usernameEntryText, passwordEntryText):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	username = usernameEntryText.get()
	password = passwordEntryText.get()
	sql = "SELECT * FROM administration WHERE username = %s AND password = %s"
	values = (username, password)
	mycursor.execute(sql, values)

	admin = mycursor.fetchone()
	if admin == None:
		print("Identifiants Incorrect !")
	else:
		print("Connexion réussie en tant que", admin)

	mydb.close()

