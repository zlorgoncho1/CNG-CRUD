import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

from functions.addLutteur import addLutteur

def calendarToggle(dateButtonText, calendar, dateIstext):
	global calendarStatus
	global row
	if not calendarStatus:
		dateButtonText.set("Récupérer la date")
		calendar.grid(row=row, column=1, pady=30)
	else:
		global date
		date = calendar.get_date()
		dateIstext.set(date)
		calendar.grid_forget()
		dateButtonText.set("Ouvrir le calendrier")

	calendarStatus = not calendarStatus

def addPage(root, switcher):
	container = tk.Frame(root, bg="white")
	container.pack(expand=True, fill=tk.BOTH)

	# --- Header ---
	header = tk.Frame(container)
	header.pack()

	title = tk.Label(header, text="Inscription", font=("Roboto", 18), bg='white', fg="black", pady=5)
	title.pack()
	# --- Header ---

	# --- Form ---
	form = tk.LabelFrame(container, text="     Formulaire     ", font=("Roboto", 12), bg='white',  fg="black")
	form.pack()

	# --- Inputs ---
	inputs = [("nom", "Nom"),("prenom", "Prenom"),("pseudo", "Pseudo"),("ecurie", "Ecurie"),("ddn", "Date de Naissance"),("nbr_combat", "Nbr Combat"),("nbr_victoire", "Nbr Victoire"),("nbr_nul", "Nbr Nul")] # Inputs

	global row
	row =  0
	# I don't like repetition
	for inputt in inputs:
		globals()[f"{inputt[0]}Frame"] = tk.Frame(form, padx=20, bg='white', pady=15) # Frame for inputs(Label and Entry)
		globals()[f"{inputt[0]}Frame"].pack()

		globals()[f"{inputt[0]}Label"] = tk.Label(globals()[f"{inputt[0]}Frame"], text=f"{inputt[1]}", font=("Roboto", 12), bg='white').grid(row=row, column=0, padx=30)

		if inputt == ("ddn", "Date de Naissance"):
			dateIstext = tk.StringVar()
			dateIstext.set("")
			dateIs = tk.Label(globals()[f"{inputt[0]}Frame"], textvariable=dateIstext, bg='white').grid(row=row, column=1)

			dateButtonText = tk.StringVar()
			dateButtonText.set("Ouvrir le calendrier")
			dateButton = tk.Button(globals()[f"{inputt[0]}Frame"], textvariable=dateButtonText, command= lambda: calendarToggle(dateButtonText, calendar, dateIstext)).grid(row=row, column=2, padx=30)

			global calendarStatus
			global date
			date = None
			calendarStatus = False
			calendar = Calendar(globals()[f"{inputt[0]}Frame"], selectmode = 'day', year = 2021, month = 12, day = 30)

		else:
			globals()[f"{inputt[0]}EntryText"] = tk.StringVar()
			globals()[f"{inputt[0]}Entry"] = tk.Entry(globals()[f"{inputt[0]}Frame"], textvariable=f"{inputt[0]}EntryText", width=20)
			globals()[f"{inputt[0]}EntryText"].set("")
			globals()[f"{inputt[0]}Entry"].grid(row=row, column=1, padx=30)

		row += 1
	# --- Inputs ---

	# --- Submit ---
	submitFrame = tk.Frame(container, bg='white')
	submitFrame.pack(pady=30)

	validerButton = tk.Button(submitFrame, text="Valider", command = lambda: addLutteur(nomEntry.get(), prenomEntry.get(), pseudoEntry.get(), ecurieEntry.get(), date, nbr_combatEntry.get(), nbr_victoireEntry.get(), nbr_nulEntry.get(), container, root, switcher), padx=40, pady=5, bg='#4EB052', fg="white", font=("Roboto", 12)).grid(row=0, column=0, padx=40)
	annulerButton = tk.Button(submitFrame, text="Annuler", command= lambda: switcher(root, switcher, container, 'indexPage'), padx=40, pady=5, bg='#DF453C', fg="white", font=("Roboto", 12)).grid(row=0, column=1, padx=40)
	# --- Submit ---

