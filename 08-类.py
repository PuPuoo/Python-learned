# 创建dog类
class Dog():
    def __init__(self, name, age):
        # 初始化name和age
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# 创建实例
my_dog = Dog('lucky',10)
print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法
my_dog.sit()
my_dog.roll_over()

