import os

empty = ""


def print_all_subdirectories(path):
    global empty
    empty += "  "
    entries = os.scandir(path)
    try:
        for entry in entries:
            if entry.name.startswith("_") or entry.name.startswith("."):
                continue
            if entry.is_dir():
                print(f"{empty}{entry.name}")
                print_all_subdirectories(entry.path)
            elif entry.is_file():
                print(f"{empty}{entry.name}")
    except Exception as f:
        print(f)
    empty = empty[:-2]


path = os.getcwd()
print_all_subdirectories(path)

# OUTPUT
'''
 01_Trash_.py
  assign_03
    10000_integers
      file_10000integers_A.txt
      file_10000integers_B.txt
    G
      11_MultiDisplayMain.py
      12_deque_main.py
      2_print_all_subdirectories.py
      5_read_numbers.py
      6_find_words.py
      8_count_numbers.py
      Deque.py
      MultiDisplay.py
      output.txt
    large_texts
      eng_news_100K-sentences.txt
      eng_news_100K-sentences_Copy.txt
      holy_grail.txt
      holy_grail_Copy.txt
    VG
      3_pretty_print_subdirectories.py
      7_count_lines.py
      9_letter_count.py
      READme.txt
  new.py
'''
