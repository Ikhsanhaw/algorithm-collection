# Python code to implement 
# Vigenere Cipher 

# This function generates the  
# key in a cyclic manner until  
# it's length isn't equal to  
# the length of original text 
def generateKey(string, key): 
    key = list(key)
    for i in range(len(string) - len(key)):
        key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the  
# encrypted text generated  
# with the help of the key 
# given plain text and key as string
def encrypt(string, key):
    if len(key) < len(string):
        newkey = generateKey(string,key)
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(newkey[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
      
# This function decrypts the  
# encrypted text and returns  
# the original text 
# given encrypted text and key as string
def decrypt(cipher_text, key):
    if len(key) < len(cipher_text):
        newkey = generateKey(cipher_text,key)
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(newkey[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))

