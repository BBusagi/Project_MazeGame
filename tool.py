def quote_chars(s):
    return ", ".join("'" + char + "'" for char in s)

# 测试函数
input_str = "####### #### ### ###     ###  ########         o### #####"
output_str = quote_chars(input_str)
print(output_str)  # 输出: '#'
