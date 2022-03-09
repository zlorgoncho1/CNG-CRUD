import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from .menu import Menu
from functions.searchLutteurs import searchLutteurs
from functions.readLutteur import readLutteur


def indexPage(root, switcher, **kwargs):

	def OnDoubleClick(event):
	    index = dataArray.item(dataArray.selection()[0], 'values')[0]
	    readLutteur(index, root, switcher, container, 'readPage')

	menu = Menu(root)

	container = tk.Frame(root, bg="white")
	container.pack(expand=True, fill=tk.BOTH)

	searchFrame = tk.LabelFrame(container, text="    Rechercher un lutteur    ", font=("Lato", 12), bg='white',  fg="black", pady=20)
	searchFrame.pack(pady=20)

	searchEntryText = tk.StringVar()
	searchEntry = tk.Entry(searchFrame, textvariable=searchEntryText, width=40)
	searchEntryText.set("")
	searchEntry.grid(row=0, column=0, padx=20)

	searchButton = tk.Button(searchFrame, text="Rechercher", command=lambda: searchLutteurs(search=searchEntry.get(), root=root, switcher=switcher, previousContainer=container, pageName='indexPage'), padx=40, bg='#3D83C3', fg="white", font=("Lato", 10)).grid(row=0, column=1, padx=20)

	addButton = tk.Button(container, text="Ajouter", command=lambda: switcher(root, switcher, container, 'addPage'), padx=40, bg="#3DC35B", fg="white", font=("Lato", 10)).pack(pady=20)

	if kwargs == {}:
		lutteurs = searchLutteurs()[0]
		message = searchLutteurs()[1]
	else:
		lutteurs = kwargs['lutteurs']
		message = kwargs['message']

	if lutteurs == []:
		textLabel = tk.Label(container, text=message, font=("Lato", 16), bg='white')
		textLabel.pack()

	else:
		s=ttk.Style()
		s.configure('Treeview', rowheight=40, height=100)

		arrayFrame = tk.Frame(container, width=300)
		arrayFrame.pack()

		columns = ('pseudo', 'ecurie', 'ddn', 'nbr_combat')
		height = len(lutteurs)
		if height < 8:
			dataArray = ttk.Treeview(arrayFrame, columns=columns, show='headings', height=height)
		else:
			dataArray = ttk.Treeview(arrayFrame, columns=columns, show='headings', height=8)

		dataArray.column('pseudo', anchor=tk.CENTER, width=150)
		dataArray.column('ecurie', anchor=tk.CENTER, width=150)
		dataArray.column('ddn', anchor=tk.CENTER, width=150)
		dataArray.column('nbr_combat', anchor=tk.CENTER, width=150)

		dataArray.heading('pseudo', text='Nom de lutteur', anchor=tk.CENTER)
		dataArray.heading('ecurie', text='Ecurie', anchor=tk.CENTER)
		dataArray.heading('ddn', text='Date de Naissance', anchor=tk.CENTER)
		dataArray.heading('nbr_combat', text='Nombre de combat', anchor=tk.CENTER)

		for lutteur in lutteurs:
			dataArray.insert('', tk.END, values=lutteur)

		dataArray.bind("<Double-1>", OnDoubleClick)

		dataArray.grid(row=0, column=0, sticky='nsew')

		scrollbar = ttk.Scrollbar(arrayFrame, orient=tk.VERTICAL, command=dataArray.yview)
		dataArray.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')
