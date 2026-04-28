import re

def tokenize(text):
    """Tokenize the user's input."""

    text_lower = text.lower()

    text_clean = re.sub(r"[-.,!?;:()\[\]{}\"']", " ", text_lower)

    text_splitted = text_clean.split()

    tokens = [t for t in text_splitted if t != "" and len(t) > 1]

    print(tokens)


texto = input("Ingrese su consulta: ")

tokenize(texto)