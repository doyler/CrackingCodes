import detectEnglish, cryptomath, time

affineCipher = __import__('9-affineCipher')

SILENT_MODE = False

def main():
    #myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    myMessage = ''

    with open("frankenstein.encrypted.affine.txt") as f:
        myMessage = f.read()

    decodedMessage = hackAffine(myMessage)

    if decodedMessage == None:
        print "Failed to break encryption."
    else:
        print "\n\nDecoded Message"
        print "--------------------"
        print decodedMessage
        print ''

def hackAffine(message):
    print "\nAttempting to decode message...\n"

    # Brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print 'Tried Key %s... (%s)' % (key, decryptedText[:40])

        startTime = time.time()
        isEnglish = detectEnglish.isEnglish(decryptedText)
        totalTime = round(time.time() - startTime, 2)
        print 'English detection time: %s seconds' % totalTime

        if isEnglish:
            print "\nPossible decrypted message:"
            print "   Key %s: %s" % (key, decryptedText[:100])
            response = raw_input("\nEnter D if done, or any other key to continue the attack: ")

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()
