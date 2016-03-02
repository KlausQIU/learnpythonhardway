import ex25_def
import ex25
def sort_words(words):
	words = sorted(words)
	return words
sentence = "All good thing come to those who wait."
words = ex25_def.break_words(sentence)
sorted_words = ex25_def.sort_words(words)

print words
print ex25_def.sort_words(words)
print ex25_def.print_first_word(words)
print ex25_def.print_last_word(words)
print ex25_def.sort_sentence(sentence)
print ex25_def.print_first_word(sorted_words)
print ex25_def.print_last_word(sorted_words)
print ex25_def.print_first_and_last(sentence)
print ex25_def.print_first_and_last_sorted(sentence)

help(ex25_def)
help(ex25_def.break_words)
help(ex25)