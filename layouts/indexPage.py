import tkinter as tk

def indexPage(root):
	container = tk.Frame(root, bg="white")
	container.pack(expand=True, fill=tk.BOTH)

	header = tk.Frame(container)
	header.pack()

	title = tk.Label(header, text="CNG | Page Index", font=("Lato", 18), bg='white', fg="black", pady=30)
	title.pack()