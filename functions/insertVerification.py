
def strHasOthersCaract(inputString):
	if any(char.isdigit() for char in inputString):
		return  True
	else:
		specialCharacters = "\"!@#$%^&*()-+?_=,<>/'"
		if any(c in specialCharacters for c in inputString):
		    return True
		else:
		    return False

def intHasOthersCaract(inputInteger):
	try:
		nombre = int(inputInteger)
		return False
	except:
		return True

def verifyCombat(nbr_combat, victoire, nul):
	combat = int(victoire) + int(nul)
	if combat > int(nbr_combat):
		return True
	return False
