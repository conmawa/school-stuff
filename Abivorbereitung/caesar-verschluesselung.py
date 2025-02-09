def caesar(word, key):
    word = word.lower()
    start = ord('a')
    for element in word:
        ascii_code = ord(element)

text = 'hallo'
caesar(text,5)