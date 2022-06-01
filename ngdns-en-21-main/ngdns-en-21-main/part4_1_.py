import BstMap
import matplotlib.pyplot as plt


def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        a = file.read()
        stringtext = a.split(" ")
        return stringtext


def popular(lst):
    words = BstMap.BstMap()
    for i in lst:
        words_value = words.get(len(i))
        if words_value is not None:
            words.put(len(i), words_value + 1)
        else:
            words.put(len(i), 1)
    return words


names2 = 'eng_news_100K-sentences_copy.txt'
eng = read_file(names2)
words = popular(eng)
lst = words.as_list()
temp_d = dict(lst)
b = temp_d.keys()
y = temp_d.values()

plt.figure(figsize=(8, 6.5))
plt.bar(b, y, align='center')
plt.title('Histogram "word length" VS "word count"')
plt.xlabel("word length")
plt.ylabel("word count")
plt.show()
