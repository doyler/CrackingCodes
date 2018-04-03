import detectEnglish

vigenereCipher = __import__('15-vigenereCipher')

def main():
    #ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    ciphertext = raw_input('\nEnter ciphertext: ')

    decodedMessage = hackVigenereDictionary(ciphertext)

    if decodedMessage == None:
        print "\nFailed to break encryption.\n"
    else:
        print "\n\nDecoded Message"
        print "--------------------"
        print decodedMessage
        print '\n'

def hackVigenereDictionary(ciphertext):
    words = ''
    with open('dictionary-fixed.txt') as f:
        words = f.readlines()

    for word in words:
        word = word.strip() # Remove the newline at the end.
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print "\nPossible decrypted message:"
            print "   Key %s: %s" % (str(word), decryptedText[:100])
            response = raw_input("\nEnter D if done, or any other key to continue the attack: ")

            if response.strip().upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
