# decimal -> binario

def tobin(n = 0):
	bin = []
	sbin = ""
	while n != 0:
		bin.insert(0, (n % 2))
		n //= 2
	for e in bin:
		sbin += str(e)
	return (sbin)