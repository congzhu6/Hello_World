def to_upper(given):
    string = " "
    for elements in given:
        if 97 <= ord(elements) <= 122:
            x = ord(elements)-32
            y = chr(x)
            string = string + y
        else:
            string = string + elements

    return string


def to_lower(given):
    string = " "
    for elements in given:
        if 65 <= ord(elements) <= 90:
            x = ord(elements) + 32
            y = chr(x)
            string = string + y
        else:
            string = string + elements

    return string


def in_reverse(given):
    string = " "
    index = len(given)
    while index > 0:
        string = string + given[index-1]
        index = index-1
    return string


def modular():
    input_string = False
    while not input_string:
        input_string = input("Enter a string to convert:\n")
        if input_string == 'STOP':
            return 'Ok, stopping'
        else:
            case = input("Enter U for uppercase and L for lower case:\n")
            if case == 'U':
                string = input_string+in_reverse(input_string)
                string = to_upper(string)
                return 'Here is your uppercase palindrome :\n' + string
            elif case == 'L':
                string = input_string+in_reverse(input_string)
                string = to_lower(string)
                return 'Here is your lowercase palindrome :\n' + string
        input_string = False


print(modular())
