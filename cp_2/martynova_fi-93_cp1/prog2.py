#Var = 10
ALPHABET = tuple(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

ALPHABET_DICT = {0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й', 10:'к',
                  11: 'л', 12: 'м', 13: 'н', 14: 'о', 15: 'п', 16: 'р', 17: 'с', 18: 'т', 19: 'у', 20: 'ф', 21: 'х', 22: 'ц',
                  23: 'ч', 24: 'ш', 25: 'щ', 26: 'ъ', 27: 'ы', 28: 'ь', 29: 'э', 30: 'ю', 31: 'я'}
#Keys:
r2 = [16, 27]
r3 = [23, 30, 5]
r4 = [6, 7, 3, 24]
r5 = [7, 19, 20, 23, 31]
r10 = [2, 4, 6, 8, 14, 26, 24, 12, 3, 9]
r11 = [6, 25, 6, 12, 7, 8, 3, 7, 27, 6, 5]
r12 = [5, 7, 3, 6, 14, 5, 3, 9, 26, 5, 2, 14]
r13 = [6, 4, 6, 4, 7, 3, 3, 8, 3, 3, 8, 28, 2]
r14 = [26, 27, 22, 8, 8, 11, 5, 24, 4, 3, 7, 4, 6, 6]
r15 = [26, 28, 7, 29, 8, 26, 28, 7, 26, 24, 6, 4, 3, 4, 12]
r16 = [4, 6, 8, 14, 26, 4, 7, 3, 3, 8, 14, 26, 31, 23, 18, 19]
r17 = [7, 3, 3, 8, 3, 9, 20, 23, 7, 29, 8, 26, 28, 7, 3, 3, 8]
r18 = [3, 6, 14, 5, 3, 9, 26, 26, 4, 7, 3, 3, 6, 12, 7, 7, 26, 24]
r19 = [4, 7, 3, 3, 19, 20, 23, 31, 7, 29, 8, 26, 2, 22, 8, 8, 14, 26, 31]
r20 = [7, 29, 8, 26, 16, 11, 7, 18, 16, 11, 8, 18, 19, 19, 16, 16, 1, 14, 23, 15]


def lower_case(char):
    if ord(char) > 1039 and ord(char) < 1072:
        char = chr(ord(char) + 32)
    return char


def exception_symbols(char):
    if ord(char) == 1105 or ord(char) == 1025:
        char = chr(1077)
    return char

def convert_chr_to_num(list, dict):
    for i in range(len(list)):
        for j in range (32):
            if list[i] == dict[j]:
                list[i] = j
                break
    return list

def convert_num_to_chr(list, dict):
    for i in range(len(list)):
        list[i] = dict[list[i]]
    return list

def enciphering(plaintext, key):
    data_list = convert_chr_to_num(plaintext, ALPHABET_DICT)
    key_len = len(key)
    cipher_data = []
    for i in range(len(data_list)):
        cipher_data.append((data_list[i] + key[i % key_len])%32)
    ciphertext = convert_num_to_chr(cipher_data, ALPHABET_DICT)
    return ciphertext

def match_index(text_list):
    n = len(text_list)
    Ind_Y = 0
    for char in text_list:
        if char in Nt_dict:
            Nt_dict[char] += 1
        else:
            Nt_dict[char] = 1
    # print(Nt_dict)
    for letter in Nt_dict.keys():
        Ind_Y += Nt_dict[letter]*(Nt_dict[letter] - 1)
    return Ind_Y/(n*(n-1))


def print_text(list):
    for i in range(len(list)):
        print(list[i], end='')

plaintext = []
letters_amount = 0
Nt_dict = {}


with open('Shakespear.txt', 'r') as text:
    for char in text.read():
        char = exception_symbols(char)
        char = lower_case(char)
        if char in ALPHABET:
            plaintext.append(char)
    print('\nYour plaintext: \n')
    print_text(plaintext)
    print(f'\nI(Y) = {match_index(plaintext)}')
    print('\n\nYour ciphertext with key length 2: \n')
    ciphertext = enciphering(plaintext, r2)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 3: \n')
    ciphertext = enciphering(plaintext, r3)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 4: \n')
    ciphertext = enciphering(plaintext, r4)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 5: \n')
    ciphertext = enciphering(plaintext, r5)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 10: \n')
    ciphertext = enciphering(plaintext, r10)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 11: \n')
    ciphertext = enciphering(plaintext, r11)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 12: \n')
    ciphertext = enciphering(plaintext, r12)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 13: \n')
    ciphertext = enciphering(plaintext, r13)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 14: \n')
    ciphertext = enciphering(plaintext, r14)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 15: \n')
    ciphertext = enciphering(plaintext, r15)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 16: \n')
    ciphertext = enciphering(plaintext, r16)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 17: \n')
    ciphertext = enciphering(plaintext, r17)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 18: \n')
    ciphertext = enciphering(plaintext, r18)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 19: \n')
    ciphertext = enciphering(plaintext, r19)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')
    print('\n\nYour ciphertext with key length 20: \n')
    ciphertext = enciphering(plaintext, r20)
    print_text(ciphertext)
    print(f'\nI(Y) = {match_index(ciphertext)}')


with open('ciphertext.txt', 'r') as text:
    for char in text.read():
        char = exception_symbols(char)
        char = lower_case(char)
        if char in ALPHABET:
            ciphertext.append(char)

    print('\nYour ciphertext: \n')
    print_text(ciphertext)
