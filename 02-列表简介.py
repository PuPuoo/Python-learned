# 列表
bicycles = ['trek','hal','asl']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# 访问最后一个元素
print(bicycles[-1])

# 修改列表元素
print(bicycles)
bicycles[0] = 'hello'
print(bicycles)

# 列表添加元素
bicycles.append('zy')
print(bicycles)
# 添加
test = []
test.append('zy')
test.append('hqy')
print(test)

# 列表插入元素
bicycles.insert(0,'hhh')
print(bicycles)

# 列表删除元素
del bicycles[0]
print(bicycles)

# pop删除元素最后一个（相当于栈顶）
pop_num = bicycles.pop()
print(bicycles)
print(pop_num)

# pop删除任意一个元素
pop_num2 = bicycles.pop(0)
print(bicycles)
print(pop_num2) 

# 根据值删除元素
test = ['hy','zy','hqy']
test.remove('hy')
print(test)

# 列表排序
test.sort()
print(test)

# 逆序
test.sort(reverse=True)
print(test)

# 临时排序
test = ['bcd','abc']
print(test)
print(sorted(test))
print(test)

# 倒着打印
print(test)
test.reverse()
print(test)

# 列表长度
print(len(test))
