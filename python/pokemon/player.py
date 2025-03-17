from name_service import NameService


class Player(NameService):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f"{self.get_name()}は走った")
