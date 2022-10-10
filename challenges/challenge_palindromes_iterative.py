def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word == "":
        return False
    reversed_word = "".join(reversed(word))
    return word == reversed_word
