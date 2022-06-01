# define a function open_file taking myFile as a parameter
def open_file(myFile):
# opening the file
    with open(myFile, 'r', encoding='utf-8') as file:
        file = file.read() # Read the file
        lst = file.split() # spliting the file
        return lst
   
# define a function unique taking word as a parameter
def unique(word):
    count = set(word) # type casting word to set
    return len(count)

# define a function occurrences taking lst as a parameter
def occurrences(lst):
    lst_words = [] # created an empty list
    for i in lst: # loop thru each character in lst
        if len(i) > 4: # checking if 
            lst_words.append(i)
    dct = {} # created an empty dictionary
    for words in lst_words:
        if words not in dct: # checking if word is in dictionary
            dct[words] = 0
        dct[words] += 1

    sort = sorted(dct.items(), key=lambda v: v[1], reverse=True)
    print('Top 10 common words larger than 4 lettersr:')
    for i in range(10): # loop thru each character in range
        print(f'{sort[i][0]} : {sort[i][1]}')
    return ''


grail = open_file('holy_grail_copy.txt')
news = open_file('eng_news_100K-sentences_copy.txt')

# printing the outputs
print(f'The number of different words in holy_grail.txt: {unique(grail)}')
print(f'The number of different words in 100K-senten.txt: {unique(news)}')

print(occurrences(grail))
print(occurrences(news))
