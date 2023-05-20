# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])


# Вывести количество букв "а" в слове
word = 'Архангельск'.lower()
letters_list = list(word)

count = 0
for letter in letters_list:
    if letter == 'а':
        count = count + 1
print(count)


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
letters_list = list(word)

count = 0

for letter in letters_list:
    if letter == 'а' or letter == 'я' or letter == 'у' or letter == 'ю' or letter == 'о' or letter == 'е' or letter == 'э' or letter == 'и' or letter == 'ы':
        count += 1
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Слов в предложении: {len(sentence.split())}')



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words_list = sentence.split()

print(words_list)

for word in words_list:
    print(word[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_list = sentence.split()

sum = 0

for word in words_list:
    sum = sum + len(word)

print(f'Средняя длина слова {round(sum / len(words_list))} символа')
