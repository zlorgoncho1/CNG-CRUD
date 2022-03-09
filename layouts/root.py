import tkinter as tk

from layouts.indexPage import indexPage
from layouts.connexionPage import connexionPage
from layouts.addPage import addPage

def root():
	root = tk.Tk()
	root.title("CNG Administration")
	root.configure(background = 'white')
	root.geometry("800x600")
	root.resizable(False, False)

	return root

def switcher(root, switcher, previousContainer, pageName, **kwargs):
	page = {"connexionPage": connexionPage, "indexPage": indexPage, "addPage": addPage}
	previousContainer.pack_forget()
	page[pageName](root, switcher, **kwargs)