class NameService:
    def __init__(self, name):
        self.__name = name

    @property
    def change_name(self):
        return self.__name

    @change_name.setter
    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
        else:
            self.__name = new_name

    def get_name(self):
        return self.__name
