b = []
for i in range(2, 101):
	for j in range(2, i):
		if i % j == 0:
			break
	else:
		print i

for a in range (0,100):
	b.append(a)

elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list."%i
	#append is a function that lists understand
	elements.append(i)

c = 2
a,b = c,c
print a,b