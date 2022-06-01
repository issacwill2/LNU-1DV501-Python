import os


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        r = file.read()
        r = r.lower()
    return r


def get_words(words):
    non_symbol = ''
    for char in words:
        if char == '\t' or char == '\n' or char.isalpha() or char == ' '\
                or char == '-' or char == "'":
            non_symbol += char
    return non_symbol.split()


def clean(words):
    new_letters = []
    for word in words:
        if len(word) == 1 and not word[0] == 'a' and not word[0] == 'i':
            continue

        if len(word) > 1 and word[0:].isalpha():
            new_letters.append(word)
    return new_letters


def save_words(file_path, words):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')


path_1 = os.getcwd()+'\\assign_03\\large_texts\\holy_grail.txt'
rows_1 = read_file(path_1)
words_1 = get_words(rows_1)
clean_words_1 = clean(words_1)
print('Reading from holy_grail.txt')
print(f'Read {len(rows_1)} lines from file --->> holy_grail.txt ')

outpath_2 = os.getcwd()+'\\assign_03\\large_texts\\holy_grail_Copy.txt'
save_words(outpath_2, words_1)
print('\n' f'saved {len(words_1)} words in file --->> holy_grail_Copy.txt')
print()

path_2 = os.getcwd()+'\\assign_03\\large_texts\\eng_news_100K-sentences.txt'
rows_2 = read_file(path_2)
words_2 = get_words(rows_2)
clean_words_2 = clean(words_2)
print('Reading from eng_new_100k-sentences.text')
print(f'\nRead {len(rows_2)} lines from file ---> eng_news_100K-sentences.txt')

outpath_2 = os.getcwd()+'\\assign_03\\large_texts\\eng_news_100K-sentences_\
Copy.txt'
save_words(outpath_2, clean_words_2)
print('\n'f'saved {len(clean_words_2)} words in file --->> eng_news_100K-\
sentences.txt')
print()

# OUTPUT
'''
Reading from holy_grail.txt
Read 72570 lines from file --->> holy_grail.txt

saved 11271 words in file --->> holy_grail_Copy.txt

Reading from eng_new_100k-sentences.text

Read 12395517 lines from file ---> eng_news_100K-sentences.txt

saved 1860387 words in file --->> eng_news_100K-sentences.txt
'''
