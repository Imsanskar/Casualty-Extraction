def convertNum(toconvert):

    toconvert = toconvert.lower()
    intconvert = text2int(toconvert)
    if intconvert.split() == toconvert.split():
        death_no = 1
        # print(death_no)
    else:
        checklist = intconvert.split(" ")
        # print(checklist)
        deathdigit = [int(s) for s in intconvert.split() if s.isdigit()]
        # print(deathdigit)
        for i in deathdigit:

            if i > 1900:
                point = checklist.index(str(i))
                checklist = checklist[point + 1:]
                dpoint = deathdigit.index(i)
                deathdigit = deathdigit[dpoint + 1:]
                # print(checklist)
                break
        if deathdigit == []:
            death_no = 1
        else:
            death_no = deathdigit[0]
    return death_no



def text2int (textnum, numwords={}):
	"""
		Calculates the number in the text
		For example:
			text2int("one two three") return six
	"""
	if not numwords:
		# units for numbers
		units = [
			"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
			"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen", "nineteen",
		]

		tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

		scales = ["hundred", "thousand", "million", "billion", "trillion"]

		numwords["and"] = (1, 0)
		for idx, word in enumerate(units):  numwords[word] = (1, idx)
		for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
		for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

	ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
	ordinal_endings = [('ieth', 'y'), ('th', '')]

	textnum = textnum.replace('-', ' ')

	current = result = 0
	curstring = ""
	onnumber = False
	for word in textnum.split():
		if word in ordinal_words:
			scale, increment = (1, ordinal_words[word])
			current = current * scale + increment
			if scale > 100:
				result += current
				current = 0
			onnumber = True
		else:
			for ending, replacement in ordinal_endings:
				if word.endswith(ending):
					word = "%s%s" % (word[:-len(ending)], replacement)

			if word not in numwords:
				if onnumber:
					curstring += repr(result + current) + " "
				curstring += word + " "
				result = current = 0
				onnumber = False
			else:
				scale, increment = numwords[word]

				current = current * scale + increment
				if scale > 100:
					result += current
					current = 0
				onnumber = True

	if onnumber:
		curstring += repr(result + current)
	return curstring