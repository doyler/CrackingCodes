import random, sys, os, primeNum, cryptomath

def main():
    # Create a public/private keypair with 1024 bit keys:
    fileName = raw_input("\nWhat would you like to name your public/private keypair: ")
    keyBits = 1024    
    makeKeyFiles(fileName, keyBits)
    print '\n\nKey files made!\n'

def generateKey(keySize):
    # Creates a public/private keys keySize bits in size.
    p = 0
    q = 0
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print '\nGenerating p & q primes...'
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e:
    print '\nCalculating d that is mod inverse of e...'
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print '\n\nPublic key: ' + str(publicKey)
    print '\nPrivate key: ' + str(privateKey)

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
    # is the value in name) with the n,e and d,e integers written in
    # them, delimited by a comma.

    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('\nWARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.\n' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print ''
    print 'The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1])))
    print 'Writing public key to file %s_pubkey.txt...' % (name)
    with open('%s_pubkey.txt' % (name), 'w') as fo:
        fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))

    print ''
    print 'The private key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1])))
    print 'Writing private key to file %s_privkey.txt...' % (name)
    with open('%s_privkey.txt' % (name), 'w') as fo:
        fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))

if __name__ == '__main__':
    main()
