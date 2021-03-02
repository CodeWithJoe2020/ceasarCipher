alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = -3
newMessage = ""


message = input("Enter a message: ")

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        #print(position)

        newPosition = (position + key) % 26
        #print(newPosition)

        newCharacter = alphabet[newPosition]
        #print(newCharacter)

        newMessage += newCharacter
    else:
        newMessage += character


print("Encrypted message is ", newMessage)