from sys import exit

def dead(why):
	print why,"GOOD JOB!"
	exit(0)

def gold_room():
	yield "This room is full of gold.How much do you take?"

	choice = raw_input(">")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man,learn to type a number.")

	if how_much < 50:
		print "Nice,you're not greedy,you win!"
		print "do you want to play again?"
		play = raw_input("Yes or no>")
		if play == "Yes" or "yes":
			start()
		else:
			exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "Thers is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input(">")

		if "take honey" in choice and not "taunt bear" in choice:
			dead("The bear looks at you then slaps your face off.")
		elif "taunt bear" in choice and not bear_moved:
			print "The bear has moved from the door.You can go through it now."
			bear_moved = True
		elif "taunt bear"  in choice and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif "open door" in choice and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He,it,whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input(">")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "which one do you take?"

	choice = raw_input(">")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
