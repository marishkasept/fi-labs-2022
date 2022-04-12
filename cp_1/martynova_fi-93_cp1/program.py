ALPHABET = tuple([' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])


def lower_case(char):
    if ord(char) > 1039 and ord(char) < 1072:
        char = chr(ord(char) + 32)
    return char


def exception_symbols(char):
    if ord(char) == 1066 or ord(char) == 1098:
        char = chr(1100)
    elif ord(char) == 1105 or ord(char) == 1025:
        char = chr(1077)
    return char


data_list = []
monogram_dict = {}
letters_amount = 0


def mono_freq(dict, num):
    for key in dict:
        dict[key] /= num
    mono_list = list(dict.items())
    mono_list.sort(key=lambda i: i[1], reverse=True)
    return mono_list


def print_mono_chart(list):
    for i in list:
        print(i[0], ':', i[1])


with open('MasterMargo.txt', 'r') as text:
    prev = 'а'
    for char in text.read():
        if char == ' ' and prev == ' ':
            continue
        prev = char
        char = exception_symbols(char)
        char = lower_case(char)
        if char in ALPHABET:
            data_list.append(char)
            if char in monogram_dict:
                monogram_dict[char] += 1
            else:
                monogram_dict[char] = 1
            letters_amount += 1
    monogram_list = mono_freq(monogram_dict, letters_amount)
    print_mono_chart(monogram_list)


def init_input_processing(data):
    pass
