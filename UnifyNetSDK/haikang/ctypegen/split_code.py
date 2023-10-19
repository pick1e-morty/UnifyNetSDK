def split_file(file_path, line_number, first_half_name, second_half_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        first_half = lines[:line_number]
        second_half = lines[line_number:]

    with open(first_half_name, 'w', encoding='utf-8') as file:
        file.writelines(first_half)

    with open(second_half_name, 'w', encoding='utf-8') as file:
        file.writelines(second_half)


# 剪切板应该没那么大，所以弄了个小脚本

# _full_headfile要切 89217
# split_file('full_headfile.py', 89217, '_most_constant.py', '_most_functions.py')

# most_constant要切 44605
split_file('_most_constant.py', 44605, '__first_half_constant.py', '__second_half_constant.py')
