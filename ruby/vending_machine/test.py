from suica_class import Suica
from vending_machine_class import VendingMachine

vm = VendingMachine()
suica = Suica()
print(f"初期金額:{suica.balance}")
vm.increase_stock()
suica.balance = 500
print(f"500円追加後のSuicaの残高:{suica.balance}")
print()

print("*" * 10 + f"ペプシ購入処理" + "*" * 10)
print(vm.restock("ペプシ", 3))
print(vm.stock("ペプシ"))
print(vm.purchase(suica, "ペプシ"))
print(suica.balance)
print(vm.stock("ペプシ"))
print()


print("*" * 10 + f"いろはす購入処理" + "*" * 10)
print(vm.restock("いろはす", 3))
print(vm.stock("いろはす"))
print(vm.purchase(suica, "いろはす"))
print(suica.balance)
print(vm.stock("いろはす"))
print()

print("*" * 10 + f"モンスター購入処理" + "*" * 10)
print(vm.restock("モンスター", 3))
print(vm.stock("モンスター"))
print(vm.purchase(suica, "モンスター"))
print(suica.balance)
print(vm.stock("モンスター"))
print()


suica.balance = 2000
for _ in range(7):
    print(vm.purchase(suica, "ペプシ"))
print(vm.purchaseable_juices())
