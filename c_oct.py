# decimal -> octal

def tooct(n = 0):
	oct = []
	soct = ""
	while n != 0:
		oct.insert(0, n % 8)
		n //= 8
	for e in oct:
		soct += str(e)
	return (soct)