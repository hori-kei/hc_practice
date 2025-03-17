from exception import VendingMachineError
from juice_class import Juice
from suica_class import Suica


class VendingMachine:

    def __init__(self):
        self.juices = []  # 在庫リスト
        self.sales = 0  # 売上金

        self.initialize_stock()

    def initialize_stock(self):
        for _ in range(5):
            self.juices.append(Juice("ペプシ", 150))

    def increase_stock(self):
        for _ in range(5):
            self.juices.append(Juice("いろはす", 120))
            self.juices.append(Juice("モンスター", 230))

    def stock(self, juice_name):
        count = sum(1 for juice in self.juices if juice.juice_name == juice_name)
        if count > 0:
            return f"{juice_name}の在庫: {count}本"
        raise VendingMachineError("指定されたジュースはありません")

    def restock(self, juice: Juice, stock: int):
        if stock <= 0:
            raise VendingMachineError("１個以上補充してください")

        for _ in range(stock):
            self.juices.append(Juice(juice.juice_name, juice.price))

        return f"{juice.juice_name}を {stock} 本補充しました"

    def sale(self, price):
        self.sales += price

    def get_juice(self, juice_name: str) -> Juice:
        for juice in self.juices:
            if juice.juice_name == juice_name:
                return juice
        raise VendingMachineError("指定されたジュースはありません")

    def purchase_check(self, suica: Suica, juice_name):
        juice = self.get_juice(juice_name)
        if suica.balance < juice.price:
            raise VendingMachineError("お金が足りません")
        return True

    def purchase(self, suica: Suica, juice_name):

        try:
            juice = self.get_juice(juice_name)
            self.purchase_check(suica, juice_name)
        except VendingMachineError as e:
            return str(e)

        suica.withdraw(juice.price)
        self.juices = [i for i in self.juices if i != juice]
        self.sale(juice.price)
        return "購入ありがとうございます"

    def purchaseable_juices(self):
        juice_list = {juice.juice_name for juice in self.juices}
        return f"購入可能なジュース: {", ".join(juice_list)}"
