MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def texto_a_morse(texto):
    morse = []
    for caracter in texto.upper():
        if caracter in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[caracter])
        elif caracter == ' ':
            morse.append(' ')
    
    return ' '.join(morse)

def morse_a_texto(morse):
    texto = []
    for palabra_morse in morse.split('  '):
        palabra = []
        for letra_morse in palabra_morse.split():
            for caracter, codigo_morse in MORSE_CODE_DICT.items():
                if codigo_morse == letra_morse:
                    palabra.append(caracter)
                    break
        texto.append(''.join(palabra))
    
    return ' '.join(texto)

def detectar_tipo(texto):
    if any(letra in MORSE_CODE_DICT for letra in texto):
        return 'morse'
    else:
        return 'texto'

def main():
    texto = input("Ingrese el texto o código Morse: ")
    tipo = detectar_tipo(texto)

    if tipo == 'texto':
        morse = texto_a_morse(texto)
        print("Texto convertido a código Morse:", morse)
    elif tipo == 'morse':
        texto = morse_a_texto(texto)
        print("Código Morse convertido a texto:", texto)
    else:
        print("Entrada no válida.")

if __name__ == "__main__":
    main()
