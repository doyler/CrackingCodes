import detectEnglish, time

transpositionDecrypt = __import__('5-transpositionDecrypt')

def main():
    #myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    myMessage = ''

    with open("frankenstein.encrypted.transposition.txt") as f:
        myMessage = f.read()

    decodedMessage = hackTransposition(myMessage)    

    if decodedMessage == None:
        print "Failed to break encryption."
    else:
        print "\n\nDecoded Message"
        print "--------------------"
        print decodedMessage
        print ''

def hackTransposition(message):
    print "\nAttempting to decode message...\n"

    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        print "Trying key #%s" % (key)

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

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
