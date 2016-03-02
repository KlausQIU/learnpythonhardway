class song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happyt_bday = song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So i'll stop right there"])

bulls_on_parade = song({"They rally around tha famil",
                        "with pockets full of shells"})
happyt_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()