import os
dir_path = os.getcwd()


def count_lines(file_path):
    lines = 0
    with open(file_path, 'r') as file_in_py:
        for line in file_in_py:
            if line.strip():
                lines += 1
    return lines


def count_py_lines(path):
    main_dir = os.scandir(path)
    all_lines = 0
    for content in main_dir:
        try:
            if content.name.startswith('.'):
                continue
            elif content.is_dir():
                all_lines += count_py_lines(content.path)
            elif content.name.endswith('.py'):
                all_lines += count_lines(content.path)

        except FileNotFoundError as error:
            print(f'FileNotFoundError:{error.filename}')

    return all_lines


print("Python Line Count:", count_py_lines(dir_path))
