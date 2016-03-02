def fab(max):
	n,a,b = 0,0,1
	while n > max:
		yield b
		a,b = b, a+b
		n = n+1

for i in range(3):
	for j in range(3):
		if i == 2:
			raise
		print i,j
except:
print "stop the error"

