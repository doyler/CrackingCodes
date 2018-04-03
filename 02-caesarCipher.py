import sys

#message = 'guv6(v6(z!(6rp5r7(zr66ntr+'
message = raw_input('\nEnter message: ')

# The encryption/decryption key:
#key = 13
key = int(raw_input("Encryption/decryption key: "))

# Whether the program encrypts or decrypts:
mode = raw_input("Would you like to encrypt or decrypt this message? ")
if mode.lower().startswith('e'): mode = "encrypt"
elif mode.lower().startswith('d'): mode = "decrypt"
else:
    print "\nMode not recognized, exiting.\n"
    sys.exit()

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/\'"'

# Stores the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

print ("\n%sed message: " + translated + "\n") % mode.title()
