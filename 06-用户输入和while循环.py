# 输入
message = input("Tell me something: ")
print(message) 

# 输入数值
age = input("How old are you?")
age = int(age)
print(age >= 18) 

# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 

# 用while在列表之间移动元素
unconfirmed_users = ['zy','pupu','hqy']
confirmed_users = []
# 只要列表不为空 一直遍历循环
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) 

# 删除包含特定值的所有列表元素
pets = ['dog','cat','dog','cat','cat']
print(pets)
# 只要cat还在列表中一直遍历下去
while 'cat' in pets:
    pets.remove('cat')
print(pets) 
