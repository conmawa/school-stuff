## Caesar - Verschlüsselung ##

def encrypt_letter(letter, key):
    letter = letter.lower()
    start = ord("a")
    end = ord("z")
    
    letter_ascii = ord(letter)
    
    new_letter = chr((letter_ascii - start + key) %26 + start)
    return new_letter

def encrypt(word, key):
    string = ""
    
    for letter in word:
        if letter.isalpha():
            string += encrypt_letter(letter, key)
        else:
            string += letter
        
    return string

def decrypt(word, key):
    string = encrypt(word, -key)
    return string

string1 = "Hello, how are you my dear friend?"
string2 = "mjqqt, mtb fwj dtz rd ijfw kwnjsi?"

print(encrypt(string1, 5))
print(decrypt(string2, 5))
    