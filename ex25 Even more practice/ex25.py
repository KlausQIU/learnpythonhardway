def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split()
	return words

def sort_words(words):
	"""sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""prints the last word after poping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sort(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


sentence = "All good things come to those who wait."
words = break_words(sentence)
print words

sorted_words = sort_words(words)
print sorted_words

#print_first_word =
print print_first_word(words)

#print_last_word = print_last_word(words)
print print_last_word(words)

print sort_sentence(sentence)

print print_first_and_last(sentence)

print print_first_and_last_sort(sentence)
