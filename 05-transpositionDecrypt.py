import math

def main():
    #myMessage = 'Cenoonommstmme oo snnio. s s c'
    #myKey = 8

    myMessage = raw_input("Please enter in the encrypted message: ")
    myKey = int(raw_input("Enter in the encryption/decryption key: "))

    plaintext = decryptMessage(myKey, myMessage)

    print '\n' + plaintext + '|\n'

def decryptMessage(key, message):
    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()
