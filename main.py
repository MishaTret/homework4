class food:
    food = "food"
    _food = "_food"
    __food = "__food"

    def __init__(self):
        self.water = "water"
        self._water = "_water"
        self.__water = "__water"

    def printer(self):
        print(self.food)
        print(self._food)
        print(self.__food)
        print(self.water)
        print(self._water)
        print(self.__water)

class printout(food):
    def hi_printer(self):
        print(self.food)
        print(self._food)
        #print(self.__food)
        print(self.water)
        print(self._water)
        #print(self.__water)


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