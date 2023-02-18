import random

class F():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __in_method(self):
        self.operacion = random.randint(1, 2)
        if self.operacion == 1:
            return self.__a + self.__b
        else:
            return self.__a - self.__b
    def printer(self):

        print(self.__in_method())

ob = F(10, 15)
ob.printer()



# class Great_Grandma:
#     height = 160
#     age = 90
#
# class Dad(Great_Grandma):
#     age = 40
#
# class Kid(Dad):
#     height = 50
#
#     def __init__(self):
#         print(f'Height - {self.height}')
#         print(f'Age - {self.age}')
#
# nick = Kid()