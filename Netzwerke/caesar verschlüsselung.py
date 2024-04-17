## Caesar-Verschlüssung ##

letters_capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
message_array = []
encrypted_message = []


def encrypt(string, key):
    for letter in string:
        message_array.append(letter)
    x = 0
    for i in range(len(message_array)):
        if message_array(i) == letters_capital(x):
            encrypted_message.append(letters_capital(x+key))
                
    print(message_array)



message = "hallo"
encrypt(message, 2)