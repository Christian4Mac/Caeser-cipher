#Caeser Cipher Encryption/Decryption

def getKey(): #gets key size from user
    key = int(input('Enter the key value:'))
    if key > 26: #ensures key is not bigger than the amount of characters in the alphabet
        print('Key size too big. Please try again.')
        getKey()
    return key #returns key as variable when function is called

def translate(phrase, key): #Hi
    cipher = "" #initializes cipher
    for cipherText in phrase: #loops for each character in 'phrase'
        cipherVal = ord(cipherText) + key #converts each character into a numeric value and shifts it up based on the key
        if cipherVal > ord('z'): #ensures values reset if they are greater than the numeric value of z
            cipherVal -= 26
        elif cipherVal < ord('a'): #ensures values reset if they are less than the numeric value of z
            cipherVal += 26
        cipherChar = chr(cipherVal) #converts the encrypted numeric values back to their now encrypted characters
        cipher += cipherChar #creates a string based on the characters
    return cipher

def encrypt(): #encryption function
    key = getKey() #assigns key variable from getKey() function
    phrase = input('Enter the cipher text or plain text:') #get plain text to encrypt
    cipher = translate(phrase, key)
    print(cipher)

def decrypt(): #decryption function
    key = getKey() #assigns key variable from getKey() function
    phrase = input('Enter the cipher text or plain text:') #get cipher text to decrypt
    cipher = translate(phrase, -key)
    print(cipher)

def caeser(): #main function, collects whether to encrypt or decrypt a phrase from the user and runs the appropriate function
    command = input('Do you wish to (e)ncrypt or (d)ecrypt a cipher?')
    if command == 'd':
        decrypt()
    elif command == 'e':
        encrypt()
    else:
        print('Invalid selection, please try again.')
        caeser()

caeser()
