from exception import VendingMachineError
from suica_class import Suica


class VendingMachine:
    # 初期状態でペプシ(150円)を5本格納している辞書
    def __init__(self):
        self.juice = {
            "ペプシ": {"price": 150, "stock": 5},
            "いろはす": {"price": 120, "stock": 5},
            "モンスター": {"price": 230, "stock": 5},
        }
        self.sales = 0

    def stock(self, juice_name):
        if juice_name in self.juice:
            stock_count = self.juice[juice_name]["stock"]
            return f"{juice_name}の在庫は{stock_count}個です"
        raise VendingMachineError("指定されたジュースはありません")

    def reduce_juice_stock(self, juice_name):
        self.juice[juice_name]["stock"] -= 1

    def sale(self, amount):
        self.sales += amount

    def purchase_check(self, suica: Suica, juice_name):
        price = self.juice[juice_name]["price"]
        stock = self.juice[juice_name]["stock"]
        if suica.balance < price:
            raise VendingMachineError("お金が足りません")
        if stock <= 0:
            raise VendingMachineError("在庫がありません")
        return True

    def purchase_process(self, suica: Suica, juice_name):
        price = self.juice[juice_name]["price"]
        try:
            self.purchase_check(suica, juice_name)
        except ValueError:
            return "購入できません"
        else:
            suica.withdraw(price)
            self.reduce_juice_stock(juice_name)
            self.sale(price)
            return "購入ありがとうございます"

    def purchaseable_juices(self):
        juice_list = [juice for juice, data in self.juice.items() if data["stock"] > 0]
        return juice_list

    def restock_juice(self, juice_name, stock):
        if juice_name in self.juice and stock > 0:
            self.juice[juice_name]["stock"] += stock
        else:
            return "無効なジュース名、または補充個数が不正です"
