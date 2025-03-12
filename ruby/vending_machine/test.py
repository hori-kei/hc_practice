from juice import Juice
from suica_class import Suica
from Vending_Machine_class import VendingMachine

vm = VendingMachine()
suica = Suica()
print(suica.balance)
suica.balance = 1000
print(suica.balance)

print(vm.purchaseable_juices())
print(vm.purchase_process(suica, "ペプシ"))
print(vm.stock("ペプシ"))
print(f"売上: {vm.sales}円")


vm.add_juice(Juice("いろはす", 120, 5))
vm.add_juice(Juice("モンスター", 230, 5))
print(vm.purchaseable_juices())
print(vm.purchase_process(suica, "ペプシ"))
print(vm.purchase_process(suica, "いろはす"))
print(vm.purchase_process(suica, "モンスター"))
print(f"売上: {vm.sales}円")
print(vm.stock("ペプシ"))
print(vm.stock("いろはす"))
print(vm.stock("モンスター"))
print(vm.restock_juice("ペプシ", 2))
print(vm.stock("ペプシ"))
print(suica.balance)
