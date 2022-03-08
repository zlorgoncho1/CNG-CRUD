import tkinter as tk
from functions.connexion import connexion

def connexionPage(root, switcher):
	
	container = tk.Frame(root, bg="white")
	container.pack(expand=True, fill=tk.BOTH)

	header = tk.Frame(container)
	header.pack()

	title = tk.Label(header, text="CNG | Page de Connexion", font=("Lato", 18), bg='white', fg="black", pady=30)
	title.pack()

	formulaire = tk.LabelFrame(container, text="     🦾Formulaire de Connexion     ", font=("Lato", 14), bg='white',  fg="black")
	formulaire.pack()

	usernameFrame = tk.Frame(formulaire, padx=20, bg='white', pady=30) 
	usernameFrame.pack()

	usernameLabel = tk.Label(usernameFrame, text="Nom d'utilisateur", font=("Lato", 16), bg='white')
	usernameLabel.grid(row=1, column=0, padx=30)

	usernameEntryText = tk.StringVar()
	usernameEntry = tk.Entry(usernameFrame, textvariable=usernameEntryText)
	usernameEntryText.set("")
	usernameEntry.grid(row=1, column=1, padx=30)


	passwordFrame = tk.Frame(formulaire, padx=20, bg='white', pady=30) 
	passwordFrame.pack()

	passwordLabel = tk.Label(passwordFrame, text="Mot de Passe", font=("Lato", 16), bg='white')
	passwordLabel.grid(row=2, column=0, padx=30)

	passwordEntryText = tk.StringVar()
	passwordEntry = tk.Entry(passwordFrame, textvariable=passwordEntryText)
	passwordEntryText.set("")
	passwordEntry.grid(row=2, column=1, padx=30)


	submitFrame = tk.Frame(container, bg='white')
	submitFrame.pack(pady=30)

	connectButton = tk.Button(submitFrame, text="Se connecter ✔", command=lambda: connexion(usernameEntryText, passwordEntryText, container, root, switcher), padx=40, pady=5, bg='white', fg="#3DC35B", font=("Roboto", 12)).grid(row=0, column=0, padx=40)
	quitButton = tk.Button(submitFrame, text="Quitter ✖", padx=40, pady=5, bg='white', fg="#C34D3D", font=("Roboto", 12)).grid(row=0, column=1, padx=40)
	# --- Submit ---
