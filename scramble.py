#Python script that searches for all possibilities of a scrambled word of it's length
#keyboard

fp = open("words.txt")
text = fp.read().lower()
wordsList = text.split()

jumbledString = str(input("Enter the jumbled letters:"))
length = len(jumbledString)
answerList = []
jword = jumbledString


for word in wordsList:
	count = 0
	count2 = 0

	if len(word) == length:
		jword = jumbledString
		
		for letter in word:

			if letter in jword:
				count += 1
				jword = jword.replace(letter, '', 1)
			
			else:
				break

		if count == length:
			print("WORD IS", word)

