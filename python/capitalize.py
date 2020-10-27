from string import ascii_lowercase, ascii_uppercase


def capitalize(str):
    if not str:
        return ""

    letter_dict = {l: u for l, u in zip(ascii_lowercase, ascii_uppercase)}
    return " ".join(letter_dict.get(s[0]) + s[1:] for s in str.split())