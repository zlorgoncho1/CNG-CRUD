import tkinter as tk

def Menu(root):

	def aidePage():
		root = tk.Tk()
		root.title("CNG Administration | Aide")
		root.configure(background = 'white')
		root.resizable(False, False)

		aide = tk.Label(root, text="Ceci est juste un projet éducatif à rendre. Juste que pour la barre de recherche, la recherche se fait par nom, prenom, pseudo, écurie").pack()


	myMenu = tk.Menu(root)
	root.config(menu=myMenu)
	
	aideMenu = tk.Menu(myMenu)
	quitMenu = tk.Menu(myMenu)

	myMenu.add_cascade(label="Aide", menu=aideMenu)
	myMenu.add_cascade(label="Quitter", menu=quitMenu)

	quitMenu.add_command(label="Quitter", command=root.quit)
	aideMenu.add_command(label="Aide", command=aidePage)

	return myMenu
