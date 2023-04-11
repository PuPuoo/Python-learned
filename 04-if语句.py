# if语句
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
print('hello' not in cars) 

# if语句
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
    print("3") 
