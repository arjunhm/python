string = input('Enter message: ').lower()
key = int(input('Enter key (0 - 26): '))

encrpyted_string = []
for letter in string:
    if ord(letter) - 97 >= (26 - key):
        val = (ord(letter) - 97) % (26 - key)
        char = chr(val + 97)

    else:
        char = chr(ord(letter) + key)
    estring.append(char)

print("".join(estring))


