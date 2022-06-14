from .database import databaseConnexion

def searchLutteurs(**kwargs):
	mydb = databaseConnexion()
	mycursor = mydb.cursor()
	message = ''
	try:
		search = kwargs['search']
		if  search == '':
			sql = "SELECT pseudo, ecurie, ddn, nbr_combat FROM lutteur"
			mycursor.execute(sql)
			lutteurs = mycursor.fetchall()
			if lutteurs == []:
				message = "Aucun lutteur ne figure dans la base de donnée.\nCommencer alors par en ajouter un !"
		else:
			sql = "SELECT pseudo, ecurie, ddn, nbr_combat FROM lutteur WHERE pseudo=%s OR ecurie=%s OR nom=%s OR prenom=%s"
			val = (search.upper(), search.upper(), search.upper(), search.upper())
			mycursor.execute(sql, val)
			lutteurs = mycursor.fetchall()
			if lutteurs == []:
				message = "Lutteur(s) introuvable"
		mydb.close()
		root = kwargs['root']
		previousContainer = kwargs['previousContainer']
		pageName = kwargs['pageName']
		kwargs['switcher'](root, kwargs['switcher'], previousContainer, pageName, lutteurs=lutteurs, message=message)

	except KeyError:
		sql = "SELECT pseudo, ecurie, ddn, nbr_combat FROM lutteur"
		mycursor.execute(sql)
		lutteurs = mycursor.fetchall()
		mydb.close()
		message = "Aucun lutteur ne figure dans la base de donnée.\nCommencer alors par en ajouter un !"
		return [lutteurs, message]