import time, os, sys

transpositionEncrypt = __import__('4-transpositionEncrypt')
transpositionDecrypt = __import__('5-transpositionDecrypt')

def main():
    #inputFilename = 'frankenstein.txt'
    inputFilename = raw_input("Please input the filename: ")

    #myKey = 10
    myKey = int(raw_input("Enter the encryption/decryption key: "))

    #myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    myMode = raw_input("Please select \"encrypt\" or \"decrypt\": ")

    outputFilename = '.'.join(inputFilename.split('.')[0:-1]) + '.' + myMode + 'ed.' + inputFilename.split('.')[-1]

    # If the input file does not exist, then the program terminates early:
    if not os.path.exists(inputFilename):
        print 'The file %s does not exist. Quitting...' % (inputFilename)
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    with open(inputFilename) as f:
        content = f.read()

    print '%sing...' % (myMode.title())

    # Measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print '%sion time: %s seconds' % (myMode.title(), totalTime)

    with open(outputFilename, 'w') as f:
        f.write(translated)

    print 'Done %sing %s (%s characters).' % (myMode, inputFilename, len(content))
    print '%sed file is %s.' % (myMode.title(), outputFilename)

if __name__ == '__main__':
    main()
