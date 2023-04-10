""" # print("hello world!")

# 变量
message = "hello world!"
print(message)

# 修改字符串大小写
name = "ada lovezy"
print(name.title())
print(name.upper())
print(name.lower())

# 字符串合并
first = "hu"
last = "qingying"
full = first + " " + last
print(full)

# 添加换行
print("hey\n\they\n\they")

# 删除空白
lan = "python "
print(lan.rstrip())

# 字符串+数字
message = "hqy" + str(13) + "zy"
print(message)

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
print(pop_num) """

""" # pop删除任意一个元素
pop_num2 = bicycles.pop(0)
print(bicycles)
print(pop_num2) """

""" # 根据值删除元素
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

# 遍历整个列表
for t in test:
    print(t) """

""" # 创建数字列表
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
print(numbers) """

""" # 切片
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
print(players) """

""" # 元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组
for d in dimensions:
    print(d) """

""" # if语句
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 检查时区分大小写
car = 'Audi'
print(car == 'audi')

# 检查不相等
res = 'hello'
if res != 'helo':
    print("wrong!")

# 检查特定值是否在列表里
print('hello' in cars)

# 检查特定值不在列表里
print('hello' not in cars) """

""" # if语句
age = 18
if age >= 18:
    print("You are odl enough!")

# if-else语句
age = 17
if age >= 18:
    print("You are old enough!")
else:
    print("Sorry!")

# if-elif-else语句
age = 12
if age < 4:
    print("1")
elif age < 18:
    print("2")
else:
    print("3") """

""" # 一个简单的字典
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建空字典
alien_0 = {}

# 再添加键值对
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改字典中的值
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])

# 删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 多行字典
favorite_languaegs = {
    'zy':'python',
    'hqy':'c++',
    }
print(favorite_languaegs)

# 遍历字典
user_0 = {
    'username':'zy',
    'first':'cy',
    'last':'hqy',
    }
for k,v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)

# 遍历字典中所有键
for k in favorite_languaegs.keys():
    print(k.title())

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languaegs.keys()):
    print(name.title())

# 遍历字典中的所有值
for language in favorite_languaegs.values():
    print(language.title())

favorite_languaegs['cy'] = 'python'
print(favorite_languaegs)

# 字典的值去重
for language in set(favorite_languaegs.values()):
    print(language)

# 嵌套
# 字典存入列表
alien_0 = {'color':'yellow','points':5}
alien_1 = {'color':'green','points':15}
alien_2 = {'color':'black','points':25}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# 列表存入字典
# 存储所点的披萨
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
for topping in pizza['toppings']:
    print(topping)

# 喜欢的语言
favorite_languaegs = {
    'zy':['python','c++','java'],
    'pupu':['java','c','python'],
    }
for name,languages in favorite_languaegs.items():
    print("\n" + name.title())
    for language in languages:
        print("\t" + language.title())

# 字典存入字典
users = {
    'zy':{
        'first':'chen',
        'last':'yu',
        'location':'fujian',
        },
    'pupu':{
        'first':'hu',
        'last':'qingying',
        'location':'hubei',
        },
    }

for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\nFull name: " + full_name.title())
    print("\tLocation: " + location.title()) """

""" # 输入
message = input("Tell me something: ")
print(message) """

""" # 输入数值
age = input("How old are you?")
age = int(age)
print(age >= 18) """

""" # while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 """

""" # 用while在列表之间移动元素
unconfirmed_users = ['zy','pupu','hqy']
confirmed_users = []
# 只要列表不为空 一直遍历循环
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) """

""" # 删除包含特定值的所有列表元素
pets = ['dog','cat','dog','cat','cat']
print(pets)
# 只要cat还在列表中一直遍历下去
while 'cat' in pets:
    pets.remove('cat')
print(pets) """
""" 
# 定义函数
def greet_user():
    print("hello!")

greet_user()

# 向函数传递信息
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user("pupu") """

# 默认值
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("lucky")

# 返回简单值
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

people = get_formatted_name('hu','qingying')
print(people)

# 让实参变成可选的
def get_name(first_name,last_name,middle_name=''):
    # middle_name默认为空字符串
    if middle_name:
        # 如果middle_name不为空，则输出
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        # 如果middle_name为空，则不输出
        full_name = first_name + " " + last_name
    return full_name

full = get_name('hu','qingying')
print(full)
full2 = get_name('hu','chen','qingying')
print(full2)

# 返回字典
def build_person(first_name,last_name):
    person = {
        'first':first_name,
        'last':last_name,
        }
    return person

people = build_person('hu','qingying')
print(people)

# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)
usersname = ['zy','pupu']
greet_users(usersname)

# 传递任意数量的实参
def make_pizza(*toppings):
    print("\nMaking a  pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('peppy')
make_pizza('zy','hqy')







