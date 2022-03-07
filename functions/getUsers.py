from .database import databaseConnexion

def getUsers():
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	sql = "SELECT pseudo, ecurie, age, nbr_combat FROM lutteur"
	mycursor.execute(sql)

	lutteurs = mycursor.fetchall()
	mydb.close()



	return lutteurs