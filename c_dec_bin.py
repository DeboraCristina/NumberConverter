# binario -> decimal

def bin_to_dec (n = ""):
	dec = 0
	aux = ""

	for e in n:
		if str (e) not in "01":
			return -1
	
	c = len(n) - 1
	while c >= 0 :
		aux += n[c]
		c -= 1 
	
	c = 0
	while c < len(n):
		dec += int(aux[c]) * 2 ** c
		c += 1
	return dec
