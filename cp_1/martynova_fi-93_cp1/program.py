from math import log2

ALPHABET = tuple([' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])

H0_mono = log2(len(ALPHABET))
H0_bi = log2(32 * 32)
print(f"For monograms H0 = {H0_mono}")
print(f"For bigrams H0 = {H0_bi}")

# H_1 = H(x1)
# H_2 = 1/2 * H(x1,x2)
# H(x1) - ентропія монограми відкритого тексту
# H(x1,x2) - ентропія біграми відкритого тексту


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


def gram_freq(dict, num):
    for key in dict:
        dict[key] /= num
    mono_list = list(dict.items())
    mono_list.sort(key=lambda i: i[1], reverse=True)
    return mono_list


def print_chart(list):
    for i in list:
        print(i[0], ':', i[1])


def mono_entropy(mono_list):
    H_1 = 0
    for char in mono_list:
        H_1 -= char[1]*log2(char[1])
    return H_1


def bi_entropy(bi_list):
    H_2 = 0
    for char in bi_list:
        H_2 -= char[1]*log2(char[1])
    return H_2/2


data_list = []
monogram_dict = {}
bigram_dict = {}
no_cross_bigram_dict = {}
letters_amount = 0
bigram_amount = 0
no_cross_bigram_amount = 0


print('\nConsidering spaces:')

with open('MasterMargo.txt', 'r') as text:
    prev = 'а'
    for char in text.read():
        if char == ' ' and prev == ' ':
            continue
        char = exception_symbols(char)
        char = lower_case(char)
        if char in ALPHABET:
            data_list.append(char)
            if char in monogram_dict:
                monogram_dict[char] += 1
            else:
                monogram_dict[char] = 1
            bigram = prev + char
            if prev != ' ' and char != ' ':
                if bigram in bigram_dict:
                    bigram_dict[bigram] += 1
                else:
                    bigram_dict[bigram] = 1
                bigram_amount += 1
            letters_amount += 1
            prev = char
    monogram_list = gram_freq(monogram_dict, letters_amount)
    bigram_list = gram_freq(bigram_dict, bigram_amount)
    print(f'\nMonogram list:\n')
    # print_chart(monogram_list)
    print(f'\nH_1 = {mono_entropy(monogram_list)}')
    print(f'\nR = {1 - mono_entropy(monogram_list)/H0_mono}')
    print(f'\nCrossing bigram list:\n')
    # print_chart(bigram_list)
    print(H0_bi)
    print(f'\nH_2 = {bi_entropy(bigram_list)}')
    print(f'\nR = {1 - bi_entropy(bigram_list) / H0_bi}')

prev = ' '
i = 0
while i < len(data_list):
    if i > 0:
        prev = data_list[i-1]
    char = data_list[i]
    if char == ' ' or prev == ' ':
        i += 1
        continue
    bigram = prev + char
    if bigram in no_cross_bigram_dict:
        no_cross_bigram_dict[bigram] += 1
    else:
        no_cross_bigram_dict[bigram] = 1
    no_cross_bigram_amount += 1
    i += 2

no_cross_bigram_list = gram_freq(no_cross_bigram_dict, no_cross_bigram_amount)
print(f'\nNo crossing bigram list:\n')
# print_chart(no_cross_bigram_list)
print(H0_bi)
print(f'\nH_2 = {bi_entropy(no_cross_bigram_list)}')
print(f'\nR = {1 - bi_entropy(no_cross_bigram_list) / H0_bi}')


ALPHABET2 = tuple(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])


data_list2 = []
monogram_dict2 = {}
bigram_dict2 = {}
no_cross_bigram_dict2 = {}
letters_amount2 = 0
bigram_amount2 = 0
no_cross_bigram_amount2 = 0

print('\nNot considering spaces:')

with open('MasterMargo.txt', 'r') as text:
    prev = ' '
    for char in text.read():
        char = exception_symbols(char)
        char = lower_case(char)
        if char in ALPHABET2:
            data_list2.append(char)
            if char in monogram_dict2:
                monogram_dict2[char] += 1
            else:
                monogram_dict2[char] = 1
            bigram = prev + char
            if prev != ' ':
                if bigram in bigram_dict2:
                    bigram_dict2[bigram] += 1
                else:
                    bigram_dict2[bigram] = 1
                bigram_amount2 += 1
            letters_amount2 += 1
            prev = char
    monogram_list2 = gram_freq(monogram_dict2, letters_amount2)
    bigram_list2 = gram_freq(bigram_dict2, bigram_amount2)
    print(f'\nMonogram list:\n')
    # print_chart(monogram_list2)
    print(f'\nH_1 = {mono_entropy(monogram_list2)}')
    print(f'\nR = {1 - mono_entropy(monogram_list2) / H0_mono}')
    print(f'\nCrossing bigram list:\n')
    # print_chart(bigram_list2)
    print(f'\nH_2 = {bi_entropy(bigram_list2)}')
    print(f'\nR = {1 - bi_entropy(bigram_list2) / H0_bi}')


i = 1
while i < len(data_list2):
    prev = data_list2[i-1]
    char = data_list2[i]
    bigram = prev + char
    if bigram in no_cross_bigram_dict2:
        no_cross_bigram_dict2[bigram] += 1
    else:
        no_cross_bigram_dict2[bigram] = 1
    no_cross_bigram_amount2 += 1
    i += 2

no_cross_bigram_list2 = gram_freq(no_cross_bigram_dict2, no_cross_bigram_amount2)
print(f'\nNo crossing bigram list:\n')
# print_chart(no_cross_bigram_list2)
print(H0_bi)
print(f'\nH_2 = {bi_entropy(no_cross_bigram_list2)}')
print(f'\nR = {1 - bi_entropy(no_cross_bigram_list2) / H0_bi}')
