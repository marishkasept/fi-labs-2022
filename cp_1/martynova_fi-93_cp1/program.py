
ALPHABET = tuple([' ','а','б','в','г','д','е','ж','з','и','й','к',
                  'л','м','н','о','п','р','с','т','у','ф','х','ц',
                  'ч','ш','щ','ы','ь','э','ю','я'])
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
    print(data_list)


def init_input_processing(data):
    pass
