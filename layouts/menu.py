import tkinter as tk

def Menu(root):
	myMenu = tk.Menu(root)
	root.config(menu=myMenu)
	
	# Menu 
	actionMenu = tk.Menu(myMenu)
	aideMenu = tk.Menu(myMenu)
	quitMenu = tk.Menu(myMenu)
	searchMenu = tk.Menu(myMenu)

	myMenu.add_cascade(label="Actions", menu=actionMenu)
	myMenu.add_cascade(label="Rechercher", menu=searchMenu)
	myMenu.add_cascade(label="Aide", menu=aideMenu)
	myMenu.add_cascade(label="Quitter", menu=quitMenu)

	# Action Menu 
	actionMenu.add_cascade(label="Ajouter")
	actionMenu.add_cascade(label="Modifier")
	actionMenu.add_cascade(label="Supprimer")

	# Search Menu 
	searchMenu.add_cascade(label="Rechercher par nom de lutteur")
	searchMenu.add_cascade(label="Rechercher par écurie")
	searchMenu.add_cascade(label="Rechercher par nombre de combat")

	return myMenu