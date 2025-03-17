from pikachu import Pikachu
from player import Player

pika = Pikachu("Pikachu", "でんき", "", 100)
satoshi = Player("satoshi")

pika.attack()
pika.change_name = "うんこ"
pika.change_name = "ピカチュウ"
print(pika.change_name)


satoshi.run()
satoshi.change_name = "うんこ"
satoshi.change_name = "サトシ"
print(satoshi.change_name)
