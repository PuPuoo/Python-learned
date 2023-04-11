# 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) 

# 文件路径
file_path = 'D:\pupu\code\python\pi_digits.txt'
with open(file_path) as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())

# 逐行读取
with open(file_path) as file_obj:
    for line in file_obj:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open(file_path) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容
with open(file_path) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 写入空文件
filename = 'programming.txt'

with open(filename,'w') as file_obj:
    file_obj.write("I Love you!") 

# 附加到文件
filename = "programming.txt"

with open(filename,'a') as file_obj:
    file_obj.write("I also love finding meaning  in large datasets.\n")
