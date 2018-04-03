from random import SystemRandom
import re

vigenereCipher = __import__('15-vigenereCipher')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NONLETTERS_PATTERN = re.compile('[^A-Z]')

def main():
    #myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    #myKey = 'ASIMOV'
    #myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

    myMessage = raw_input('\nEnter message: ')
    #myKey = raw_input("Encryption/decryption key: ")
    myKey = getRandomKey(len(NONLETTERS_PATTERN.sub('', myMessage)))
    myMode = raw_input("Would you like to \"encrypt\" or \"decrypt\" this message? ")

    if myMode == 'encrypt':
        translated = vigenereCipher.encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = vigenereCipher.decryptMessage(myKey, myMessage)

    print '\n%sed message:' % (myMode.title())
    print translated
    print ''

def getRandomKey(length):
    gen = SystemRandom()
    return ''.join([gen.choice(LETTERS) for i in range(length)])

if __name__ == '__main__':
    main()


