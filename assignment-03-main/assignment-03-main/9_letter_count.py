import os

file_path_1 = os.getcwd()+'\\assign_03\\large_texts\\holy_grail_Copy.txt'
file_path_2 = os.getcwd()+'\\assign_03\\large_texts\\eng_news_100K-\
sentences.txt'
text_files = [file_path_1, file_path_2]

chars = "abcdefghijklmnopqrstuvwxyz"
for file_name in text_files:
    dic = {}
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip().lower()
            for char in text:
                if char in chars:
                    if char in dic.keys():
                        dic[char] += 1
                    else:
                        dic[char] = 1
    print(f"Reading text from the file: {file_name}")
    print(f"Total number of characters: {sum(dic.values())}")
    smb = min(dic.values())
    print(f"Histogram where each star represents {smb} occurrences.")
    for letter in sorted(dic.keys()):
        print("{} | {}".format(letter, "*" * int(dic[letter] / smb)))
