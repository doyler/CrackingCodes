#message = 'guv6(v6(z!(6rp5r7(zr66ntr+'
message = raw_input('\nEnter message: ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/\'"'

print ''

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    translated = ''

    # Loop through each symbol in `message`:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print 'Key #%s: %s' % (key, translated)

print ''
