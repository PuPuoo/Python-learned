# 定义函数
def greet_user():
    print("hello!")

greet_user()

# 向函数传递信息
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user("pupu") 

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

# 传递多个键值对，字典接收
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile

user_profile = build_profile('hu','qingying',location = 'hubei',field = 'wuhan')
print(user_profile)

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
# 导入整个模块
import pizza

pizza.make_pizza(16,'peppy')
pizza.make_pizza(5,'mashroom')

# 导入特定的函数
from pizza import make_pizza

make_pizza(16,'haha')

# 使用as给函数指定别名
from pizza import make_pizza as mp

mp(16,'pupu')

# 使用as给模块指定别名
import pizza as p

p.make_pizza(16,'zy')

# 导入模块中的所有函数
from pizza import *

make_pizza(17,'xixi')


