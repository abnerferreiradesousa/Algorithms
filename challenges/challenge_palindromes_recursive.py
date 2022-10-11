def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if low_index < len(word):
        other_word = word[low_index] == word[high_index]

    if word == "" or other_word is False:
        return False

    if low_index >= high_index:
        return True

    if other_word:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
