from pokemon import Pokemon


class Pikachu(Pokemon):

    def attack(self):
        super().attack()
        print(f"{self.get_name()}の10万ボルト")
