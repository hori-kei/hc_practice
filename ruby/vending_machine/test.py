from juice_class import VendingMachine
from suica_class import Suica

# Suica と VendingMachine のインスタンスを作成
suica = Suica()
vm = VendingMachine()

# 現在の残高と在庫を表示
print(f"初期残高: {suica.balance}円")  # 500円
print(vm.stock("ペプシ"))  # 在庫 5 個

# ペプシを購入
print(vm.purchase_process(suica, "ペプシ"))

# 購入後の残高と在庫を表示
print(f"購入後の残高: {suica.balance}円")  # 350円
print(vm.stock("ペプシ"))  # 在庫 4 個

suica.balance = 1000  # 1000円をチャージ
print(f"残高:{suica.balance}円")  # 残高を表示  # 残高1350円

print(vm.purchase_process(suica, "ペプシ"))
print(vm.purchase_process(suica, "いろはす"))
print(vm.purchase_process(suica, "モンスター"))
print(vm.restock_juice("いろはす", 5))
print(vm.stock("いろはす"))
print(vm.purchaseable_juices())
print(vm.purchase_process(suica, "ペプシ"))
print(vm.purchase_process(suica, "ペプシ"))
print(vm.purchase_process(suica, "ペプシ"))
print(vm.purchaseable_juices())
