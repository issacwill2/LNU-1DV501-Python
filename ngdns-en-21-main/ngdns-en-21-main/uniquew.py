import BstMap as BM
import HashSet as HS


def read_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        a = file.read()
        stringtext = a.split(" ")
        return stringtext


names = r'holy_grail_copy.txt'
holy_rows = read_file(names)

names2 = 'eng_news_100K-sentences_copy.txt'
rows_100 = read_file(names2)


def hash_set(lst):
    a = HS.HashSet()
    a.init()
    for i in lst:
        a.add(i)
    return a


def popular(lst):
    words = BM.BstMap()
    for i in lst:
        if len(i) <= 4:
            continue
        words_value = words.get(i)
        if words_value is not None:
            words.put(i, words_value + 1)
        else:
            words.put(i, 1)
    counts = sorted(words.as_list(), key=lambda v: v[1], reverse=True)
    print("Top 10 used words larger than 4 letters:")
    for i in range(10):
        print(f'{counts[i][0]} : {counts[i][1]}')
    print("\nMax depth :", words.max_depth())
    return " "


holy_hash_set = hash_set(holy_rows)
print("\nHoly grail elements size:", holy_hash_set.get_size())
print("Holy grail max buckets:", holy_hash_set.max_bucket_size(), "\n")

holy_grail = read_file(names)
print(popular(holy_grail))

eng_hash_set = hash_set(rows_100)
print("\nEng news 100k sentences elements size:", eng_hash_set.get_size())
print("Eng 100k sentences max buckets:", eng_hash_set.max_bucket_size(), "\n")

eng_news = read_file(names2)
print(popular(eng_news))
