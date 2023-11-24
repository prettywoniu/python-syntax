def print_upper_words(words, must_start_with):
	'''Given a list of words, print each word that starts with character in 
	   the second argument must_start_with, in uppercase on a separate line.

		For example:
		print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

        Should print
        HELLO 
        HEY
        YO
        YES
	   '''

	for word in words:
		upWord = word.upper()
		tmp = list()

		for s in must_start_with:
			tmp.append(s.upper())

		starts = tuple(tmp)
		if upWord.startswith(starts):
			print(upWord)



#print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})