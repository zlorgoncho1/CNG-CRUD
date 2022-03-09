from layouts.root import root, switcher
from layouts.indexPage import indexPage

if __name__ == '__main__':
	root = root()
	indexPage(root, switcher)
	root.mainloop()