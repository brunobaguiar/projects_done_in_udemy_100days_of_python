to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '.': '.-.-.-',
    '?': '..--..', ',': '--..--', ' ': '/'
}


def to_morse_code():
    string = input("Type the sentence you want to translate to morse code: ")
    morse_code = ""
    for letter in string:
        morse_code += to_morse[letter.lower()] + " "
    return morse_code


print(to_morse_code())
