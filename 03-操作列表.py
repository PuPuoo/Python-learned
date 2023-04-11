# 遍历整个列表
for t in test:
    print(t) 

# 创建数字列表
for value in range(1,6):
    print(value)

# list创建列表
numbers = list(range(1,6))
print(numbers)

# 指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

# 平方
numbers = []
for t in range(1,11):
    num = t**2
    numbers.append(num)
print(numbers)

# 最值
numbers = [1,2,3,4,5,6,7,8,9,0]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表解析
numbers = [value**2 for value in range(1,11)]
print(numbers) 

# 切片
players = ['zy','hqy','cy','haha']
print(players[0:3])

# 从头开始
print(players[:3])

# 直到末尾
print(players[1:])

# 末尾三个
print(players[-3:])

# 遍历切片
for player in players[:3]:
    print(player.title())

# 复制列表
my_players = players[:]
print(my_players)
print(players) 

# 元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组
for d in dimensions:
    print(d) 
