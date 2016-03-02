list = ["1","2"]
assert len(list) >= 2
print  list


def gold_room():
	yield "Good jOB!"

gold_room()

def fab(max):
	n,a,b = 0,0,1
	while n > max:
		yield b
		a,b = b, a+b
		n = n+1
fab(6)