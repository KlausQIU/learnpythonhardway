animals = ['bear','python','peacock','kangaroo','whale','platypus',"monkey"]

b = len(animals)
print "the animals of type is :%r type"%b
for i in range(0,b):
	print "the %r type is:"%i,":",animals[i]
	if i < len(animals):
		i += 1
	else:
		break


