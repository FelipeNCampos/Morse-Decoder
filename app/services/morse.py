"""Conversão entre texto e código Morse internacional."""

import unicodedata


MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-",
    ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "@": ".--.-.",
}

TEXT_CODE = {code: character for character, code in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    """Converte texto para Morse; palavras são separadas por barra (/)."""
    normalized = unicodedata.normalize("NFD", text.upper())
    characters = [char for char in normalized if not unicodedata.combining(char)]
    result = []

    for character in characters:
        if character.isspace():
            result.append("/")
        elif character in MORSE_CODE:
            result.append(MORSE_CODE[character])
        else:
            raise ValueError(f"Caractere não suportado: {character}")

    return " ".join(result)


def morse_to_text(morse: str) -> str:
    """Converte Morse para texto; use / para separar palavras."""
    result = []

    for code in morse.split():
        if code == "/":
            result.append(" ")
        elif code in TEXT_CODE:
            result.append(TEXT_CODE[code])
        else:
            raise ValueError(f"Código Morse inválido: {code}")

    return "".join(result)
