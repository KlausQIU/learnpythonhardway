print "please enter door number."print "You enter a dark room with two doors.Do you through door #1 or door #2?"


door = raw_input(">")

if door == "1":
	print "That 's a gaint bear hear eating a cheese cake.what do you do?"
	print "1,Take the cake."
	print "2,scream at the bear."

	bear = raw_input(">")

	if bear == "1":
	    print "the bear eats your face off.good job!"
	elif bear == "2":
		print "the bear eats your legs off.good job!"
	else:
		print "well,doing %s is probably better.Bear runs away."% bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1.Blueberries."
	print "2,Yellow jacket clothespins."
	print "3,Understanding revolvers yelling melodies."

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.good job!"
	else:
		print "The insanity rots your eyes into a pool of much.good job!"

else:
    print "You stunble around and fall on a knife and die.good job!"
