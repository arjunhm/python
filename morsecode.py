
# A simple morse code converter program

import sys
myList = []
encodeList = []
decodeList = []

fp = open('morse.txt')
txt = fp.read()
myList = txt.split('\n')

def decodeText(morseWord):
	
	for word in myList:

		if morseWord in word:

			if len(morseWord)==len(word[2:]):
				return(word[0])


def encodeText(letter):

	for word in myList:

		if word[0] == letter:
			return(word[2:])


while(1):

	print("MORSE CODE CONVERTER")
	print("Do you wish to")
	print("1. Encode")
	print("2. Decode")
	print("3. Exit")
	choice = int(input())

	if choice == 1:
		normalText = (input('Enter message to be encoded:')).upper()
		for letter in normalText:

			if letter.isalpha():
				encodeLetter = encodeText(letter)
				encodeList.append(encodeLetter)

		encodeText = " ".join(encodeList)
		print(encodeText)
		print('\n'*2)

	elif choice == 2:
		codeText = input('Enter message to be decoded:')
		codeTextList = codeText.split()

		for morseWord in codeTextList:
			decodeLetter = decodeText(morseWord)
			decodeList.append(decodeLetter)
		
		decodedText = "".join(decodeList)
		print(decodedText)
		print('\n'*2)

	elif choice == 3:
		sys.exit()

	else:
		print('Invalid choice')
