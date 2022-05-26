# decimal -> hexdecimal

def tohex(n = 0):
	hex = []
	shex = ""
	tabhex = ["A", "B", "C", "D", "E", "F"]
	while n != 0:
		r = n % 16
		if r >= 10:
			hex.insert(0, tabhex[r % 10])
		else:
			hex.insert(0, r)
		n //= 16
	for e in hex:
		shex += str(e)
	return (shex)