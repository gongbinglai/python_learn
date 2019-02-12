
class Animal():

    def __init__(self, name, age):  # 注意,后面一定要有空格
        self.__name = name
        self.__age = age

    def who_ami(self):
        print("i am Animal")

    def print_animal(self):
        print(self.__name+","+str(self.__age))


class Cat(Animal):

    def __init__(self, name, age):
       super().__init__(name, age)

    def who_ami(self):
        print("i am Cat")

# 多继承，尽量避免多继承
# class ShortCat(Animal,Cat):
#
#     def __init__(self, name, age):
#        super().__init__(name, age)
#
#     def who_ami(self):
#         print("i am ShortCat")



a1 = Animal('Animal',10)

a2= Cat('Cat',20)

a1.print_animal()
a2.print_animal()


a1.who_ami()
a2.who_ami()












































