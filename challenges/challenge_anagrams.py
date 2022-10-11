def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    list_counter_letters = []

    # Case One
    # pedrra ==== pedraa
    # list_counter_letters = ["p", "e", "d", "r", "a"]

    for letter in first_string.lower():
        if (
            letter in second_string.lower()
            and letter not in list_counter_letters
        ):
            list_counter_letters.append(letter)
            first_string = "".join(list_counter_letters)

    if len(first_string) == len(second_string):
        return True
    return False
