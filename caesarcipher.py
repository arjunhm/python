"""
The Caesar cipher is a substitution cipher where each letter in the original message is replaced with a letter corresponding to a certain number of letters up or down in the alphabet. 
"""

string = str(input('Enter the message to be encrypted:\n').lower())

others = 'yz'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ['']

key = int(input("Enter key(0-26):"))
dstring = []


def encryptString(string, key):

	enstring = []
	for i in string:

		if i in alphabet[0: key]:
			char = chr(ord(i) + (26 - key))
			enstring.append(char)

		elif i in alphabet:
			char = chr(ord(i) - key)
			enstring.append(char)

		else:
			char = i
			enstring.append(char)

return enstring


def decryptString(string, key):

	dstring = []
	for i in string:
		if i in alphabet[(26-key): 26]:
			char = chr(ord(i) - (26 - int(key)))
			dstring.append(char)

		elif i in alphabet:
			char = chr(ord(i)+key)
			dstring.append(char)

		else:
			char = i
			dstring.append(char)			
	return dstring

enstring = encryptString(string, key)
print('\nEncrypted message is')
print(''.join(enstring))

"""
dstring = decryptString(enstring,key)
print(''.join(dstring))
"""
