def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # print(f"Word -> {word} --- LI -> {low_index} --- HI -> {high_index}")
    # Word -> REVIVER --- LI -> 0 --- HI -> 199

    if low_index < len(word):
        other_word = word[low_index] == word[high_index]

    if word == "" or other_word == False:
        return False

    if low_index >= high_index:
        return True

    if other_word == True:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
