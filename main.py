# 获取用户输入的一行字符
input_string = input()

# 初始化四个变量来分别存储英文字符、数字、空格和其他字符的数量
english_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 遍历输入的字符串中的每个字符
for char in input_string:
    if char.isalpha():
        # 如果字符是字母，则英文字符数量加 1
        english_count += 1
    elif char.isdigit():
        # 如果字符是数字，则数字数量加 1
        digit_count += 1
    elif char.isspace():
        # 如果字符是空格，则空格数量加 1
        space_count += 1
    else:
        # 否则，其他字符数量加 1
        other_count += 1

# 按照要求的格式输出统计结果
print(f"英文字符:{english_count}")
print(f"数字:{digit_count}")
print(f"空格:{space_count}")
print(f"其他字符:{other_count}")# 这个文件用于编写代码
