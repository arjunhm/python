"""
This program takes a letter or few letters as input and displays the possible letters that can be appended to the input to form a word
"""

import sys
fp=open("words.txt")
text=fp.read()
wordsList=text.split()

myList=[]

answer=1
string=''

while answer!=3:
	if answer==2:
		print("Search word has been reset\n")
		string=''
	print("Enter search word:")
	print(string)
	string=string+str(input(""))

	myList.clear()
	for word in wordsList:
		if word.startswith(string):
			if not word[len(string):len(string)+1] in myList:
				myList.append(word[len(string):len(string)+1])

	if len(myList)==0:
		print(string[:len(string)-1])
		print("No word found\n")		
		answer=2
		continue
	else:		
		print(myList)
	print()
	answer=int(input("Do you wish to\n1. Continue\n2. Restart\n3. Exit?:\n"))
