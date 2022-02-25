import tkinter as tk

def root():
	root = tk.Tk()
	root.title("CNG Administration")
	root.configure(background = 'white')
	root.geometry("800x600")
	root.resizable(False, False)

	return root