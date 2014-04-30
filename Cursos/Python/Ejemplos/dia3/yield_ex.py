def contador(max):
	n = 0
	while n<max:
		yield n
		n+=1

def get_pares(max):
	n = 1
	while n<max:
		if n%2==0:
			yield n
		n+=1


def multiples_yield():
	yield 1
	yield 2
	yield 3

def multiples_yield2():
	while True:
		yield 1
		yield 2
		yield 3
