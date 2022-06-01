import os

space = ""


def print_all_subdirectories(dir_path):
    global space
    space += "  "
    sub_dirs = os.scandir(dir_path)
    try:
        for i in sub_dirs:
            if i.name.startswith("_") or i.name.startswith("."):
                continue
            if i.is_dir():
                print(f"{space}{i.name}")
                print_all_subdirectories(i.path)
            elif i.is_file():
                print(f"{space}{i.name}")
    except Exception as f:
        print(f)


path = os.getcwd()
print(path)
print_all_subdirectories(path)

# OUTPUT
'''
C:\\Users\\issac\\Documents\\1dv501.03
  01_Trash_.py
  7_count_lines.py
  9_letter_count.py
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
        Deque_output.txt
        G_ALL_Output.txt
        MultiDisplay.py
        large_texts
          eng_news_100K-sentences.txt
          eng_news_100K-sentences_Copy.txt
          holy_grail.txt
          holy_grail_Copy.txt
          VG
            3_pretty_print_subdirectories.py
            READme.txt
            new.py
            try.py
'''
