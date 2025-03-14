from exception import VendingMachineError
from juice_class import Juice
from suica_class import Suica


class VendingMachine:

    def __init__(self):
        self.juices = []  # 在庫リスト
        self.sales = 0  # 売上金

        # 初期状態でペプシ、いろはす、モンスターを5本ずつ追加
        self.initialize_stock()

    def initialize_stock(self):
        """初期在庫でペプシを5本追加"""
        for _ in range(5):
            self.juices.append(Juice("ペプシ", 150))

    def increase_stock(self):
        for _ in range(5):
            self.juices.append(Juice("いろはす", 120))
            self.juices.append(Juice("モンスター", 230))

    def stock(self, juice_name):
        """指定されたジュースの在庫数を取得"""
        count = sum(1 for juice in self.juices if juice.juice_name == juice_name)
        if count > 0:
            return f"{juice_name}の在庫: {count}本"
        raise VendingMachineError("指定されたジュースはありません")

    def restock(self, juice_name, stock):
        """ジュースを補充する"""
        if stock <= 0:
            raise VendingMachineError("１個以上補充してください")

        for _ in range(stock):
            if juice_name == "ペプシ":
                self.juices.append(Juice("ペプシ", 150))
            elif juice_name == "いろはす":
                self.juices.append(Juice("いろはす", 120))
            elif juice_name == "モンスター":
                self.juices.append(Juice("モンスター", 230))
            else:
                raise VendingMachineError("指定されたジュースはありません")

        return f"{juice_name}を {stock} 本補充しました"

    def sale(self, price):
        self.sales += price

    def purchase_check(self, suica: Suica, juice_name):
        # 在庫確認
        if not any(juice.juice_name == juice_name for juice in self.juices):
            raise VendingMachineError("在庫がありません")

        # 価格確認
        for juice in self.juices:
            if juice.juice_name == juice_name:
                if suica.balance < juice.price:
                    raise VendingMachineError("お金が足りません")
                return True

        raise VendingMachineError("指定されたジュースはありません")

    def purchase(self, suica: Suica, juice_name):
        """ジュースを購入する"""
        for juice in self.juices:
            if juice.juice_name == juice_name:
                try:
                    if not self.purchase_check(suica, juice_name):
                        return "購入できません"
                except VendingMachineError as e:
                    return str(e)

                suica.withdraw(juice.price)
                self.juices = [i for i in self.juices if i != juice]
                self.sale(juice.price)
                return "購入ありがとうございます"

    def purchaseable_juices(self):
        juice_list = {juice.juice_name for juice in self.juices}
        return f"購入可能なジュース: {", ".join(juice_list)}"
