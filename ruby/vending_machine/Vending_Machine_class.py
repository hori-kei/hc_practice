from exception import VendingMachineError
from juice import Juice
from suica_class import Suica


class VendingMachine:
    # 初期状態でペプシ(150円)を5本格納している辞書
    def __init__(self):
        self.juices = []
        self.sales = 0

        # ↓はtupleでデータ管理しているんじゃない、Juiceクラスでペプシインスタンスを作成した。
        self.add_juice(Juice("ペプシ", 150, 5))

    def add_juice(self, juice):
        self.juices.append(juice)

    def stock(self, juice_name):
        for juice in self.juices:
            if juice.juice_name == juice_name:
                return f"{juice_name}の在庫:{juice.stock}"
        raise VendingMachineError("指定されたジュースはありません")

    def sale(self, price):
        self.sales += price

    def purchase_check(self, suica: Suica, juice_name):
        for juice in self.juices:
            if juice.juice_name == juice_name:
                price = juice.price
                stock = juice.stock
                if suica.balance < price:
                    raise VendingMachineError("お金が足りません")
                if stock <= 0:
                    raise VendingMachineError("在庫がありません")
                return True
        raise VendingMachineError("指定されたジュースはありません")

    def purchase_process(self, suica: Suica, juice_name):
        for juice in self.juices:
            if juice.juice_name == juice_name:
                price = juice.price
                try:
                    if not self.purchase_check(suica, juice_name):
                        return "購入できません"
                except VendingMachineError as e:
                    return str(e)
                else:
                    suica.withdraw(price)
                    juice.reduce_juice_stock()
                    self.sale(price)
                    return "購入ありがとうございます"
        raise VendingMachineError("指定されたジュースはありません")

    def restock_juice(self, juice_name, stock):
        for juice in self.juices:
            if juice.juice_name == juice_name:
                juice.restock(stock)
            return f"{juice_name}の在庫を {stock} 個補充しました"

        raise VendingMachineError("指定されたジュースはありません")

    def purchaseable_juices(self):
        juice_list = [juice.juice_name for juice in self.juices if juice.stock > 0]
        return f"購入可能なジュース: {", ".join(juice_list)}"
