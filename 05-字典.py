# 一个简单的字典
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
    print("\tLocation: " + location.title()) 
