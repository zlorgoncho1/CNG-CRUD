from .database import databaseConnexion

def getLutteurs():
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	sql = "SELECT pseudo, ecurie, ddn, nbr_combat FROM lutteur"
	mycursor.execute(sql)

	lutteurs = mycursor.fetchall()
	mydb.close()

	return lutteurs
