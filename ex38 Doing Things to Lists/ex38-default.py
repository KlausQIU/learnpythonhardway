# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "items:%s"%ten_things
print "Wait! there are not 10 things in that list.Let's fix that."

stuff = ten_things.split(' ')  #还是要加空格
more_stuff = ['Day','Night','Song','Frisbee','Corn','Banana','Girl','Boy']

'''
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding:",next_one
	stuff.append(next_one)
	print"There are %d items now."%len(stuff)
'''
a = len(stuff)
for a in range(0,10):
	if a < 10:

	print"There are %d items now."%len(stuff)
print "There we go:",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print '-'.join(stuff)
print '-'.join(stuff[3:5])
