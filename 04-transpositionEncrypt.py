def main():
    #myMessage = '''Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer.'''
    #myKey = 13

    myMessage = raw_input("Please enter in the message to encrypt: ")
    myKey = int(raw_input("Enter in the encryption/decryption key: "))

    ciphertext = encryptMessage(myKey, myMessage)

    print ciphertext + '|'

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
