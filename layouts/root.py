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

def switcher(root, switcher, previous_container, page_name):
	page = {"connexionPage": connexionPage, "indexPage": indexPage, "addPage": addPage}
	previous_container.pack_forget()
	page[page_name](root, switcher)