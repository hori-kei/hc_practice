from name_service import NameService


class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name)
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.get_name()}の攻撃！")
