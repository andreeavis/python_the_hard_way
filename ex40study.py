class MySong(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def play_song(self):
		for line in self.lyrics:
			print(line)


# eminem_stan = MySong(["The tea's run cold, I wonder why",
# 					"Got out of bed at all",
# 					"The morning rain clouds up my window",
# 					"And I can't see at all",
# 					"But even if I could it would all be gray",
# 					"But your picture on my wall",
# 					"It reminds me, that it's not bad, it's not so bad"
# 					])


# pink_sober = MySong(["I'm safe, up high, nothing can touch me",
# 					"But why I feel this party's over",
# 					"No pain inside, you're my protection",
# 					"But how do I feel so good sober"
# 					])


# gwen_just_a_girl = MySong(["'Cause I'm just a girls, the little ol' me",
# 						   "Well don't let me out of your sight",
# 						   "Oh, I'm just a girl, all pretty and petite",
# 						   "So don't let me have any rights",
# 						   "Oh, I've had it up to here!"
# 							])

# aretha_respect = MySong(["R-E-S-P-E-C-T",
# 						"Find out what it means to me",
# 						"R-E-S-P-E-C-T",
# 						"Take care, TCB"
# 						])

# eminem_stan.play_song()
# print("<>" * 10)
# pink_sober.play_song()
# print("<>" * 10)
# gwen_just_a_girl.play_song()
# print("<>" * 10)
# aretha_respect.play_song()


# my_lyrics = (["'Cause I'm just a girls, the little ol' me",
#  						   "Well don't let me out of your sight",
#  						   "Oh, I'm just a girl, all pretty and petite",
#  						   "So don't let me have any rights",
#  						   "Oh, I've had it up to here!"
#  							])

# gwen_just_a_girl = MySong(my_lyrics)
# print(gwen_just_a_girl.play_song())