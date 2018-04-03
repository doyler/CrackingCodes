LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    #myKey = 'ASIMOV'
    #myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    myMessage = raw_input('\nEnter message: ')
    myKey = raw_input("Encryption/decryption key: ")
    #myKey = getRandomKey()
    myMode = raw_input("Would you like to \"encrypt\" or \"decrypt\" this message? ")

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print '\n%sed message:' % (myMode.title())
    print translated
    print ''

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] # Stores the encrypted/decrypted message string.

    keyIndex = 0
    key = key.upper()

    for symbol in message: # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting.

            num %= len(LETTERS) # Handle any wraparound.

            # Add the encrypted/decrypted symbol to the end of translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return ''.join(translated)

if __name__ == '__main__':
    main()
