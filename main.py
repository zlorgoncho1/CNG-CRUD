from layouts.root import root, switcher
from layouts.connexionPage import connexionPage

if __name__ == '__main__':
	root = root()
	connexionPage(root, switcher)
	root.mainloop()