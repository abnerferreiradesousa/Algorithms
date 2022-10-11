def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    # Case One
    # pedrra ==== pedraa
    # list_counter_letters = ["p", "e", "d", "r", "a"]

    if len(first_string) != len(second_string):
        return False
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())
    for letter in first_string_list:
        try:
            second_string_list.remove(letter)
        except ValueError:
            return False
    return True

    # Version one...
    # list_counter_letters = []
    # for letter in first_string.lower():
    #     if (
    #         letter in second_string.lower()
    #         and letter not in list_counter_letters
    #     ):
    #         list_counter_letters.append(letter)
    #         first_string = "".join(list_counter_letters)

    # if len(first_string) == len(second_string):
    #     return True
    # return False
