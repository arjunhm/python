from random import randint
import sys

fp = open('words.txt')
txt = fp.read()			

text = txt.split()
words = []
qw = []


for word in text:

	if word.isalpha():
		words.append(word)


def generateWord():
	num = randint(0, 25371)		
	return words[num].lower()


def setWord(word):
	qwl = []
	for x in range(0, len(word)):

		if word[x] in ['a', 'e', 'i', 'o', 'u']:
			qwl.append(word[x])

		else:
			qwl.append('-')

	return qwl


def guessLetter(letter, word, qw):
	flag = False

	for x in range(0, len(word)):
		if word[x] == letter:
			qw[x] = letter
			flag = True

	print(''.join(qw))
	return flag

word = generateWord()

qw = setWord(word)
print(''.join(qw))
flag = True
count = 0

while count < 5:
	letter = input("Enter a letter: ")
	flag = guessLetter(letter, word, qw)

	if flag == False:
		count += 1

	if word == ''.join(qw):
		print("You win")
		sys.exit()

print("You lose")
print("Correct word is {}".format(word))
