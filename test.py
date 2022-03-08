def test():
	def test2():
		print('Hey')
	a = 3
	return[a, test2]

func = test()[1]
func()