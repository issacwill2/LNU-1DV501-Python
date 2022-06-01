import HashSet
import matplotlib.pyplot as plt


def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        a = file.read()
        stringtext = a.split(" ")
        return stringtext


def hash_set(lst):
    a = HashSet.HashSet()
    a.init()
    for i in lst:
        a.add(i)
    return a


names2 = 'eng_news_100K-sentences_copy.txt'
eng_news = read_file(names2)
eng = read_file(names2)


un = hash_set(eng_news)
len_all = len(eng)

uniques = un.get_size()
adds = len_all


x = ["added words", "unique words"]
y = [adds, uniques]
plt.figure(figsize=(8, 6.5))
plt.bar(x, y, align='center')
plt.title('"added words" VS "unique words"')
plt.xlabel("added words and unique words")
plt.ylabel("words")
plt.show()
