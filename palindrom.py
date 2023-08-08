# Палиндром - строка, которая читается одинаково как слева направо, так и справа налево


def palindrom(string):
    string = string.lower()
    str_rev = ''
    for word in string:
        str_rev = word + str_rev
    if str_rev == string:
        return True
    return False

# Сразу для проверки:
line = input('Введите строку, чтобы узнать, палиндром ли это?')
print(palindrom(line))
