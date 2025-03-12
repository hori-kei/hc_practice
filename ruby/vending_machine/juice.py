from exception import VendingMachineError


class Juice:

    def __init__(self, juice_name, price, stock):
        self.juice_name = juice_name
        self.price = price
        self.stock = stock

    def reduce_juice_stock(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            raise VendingMachineError("在庫がありません")

    def restock(self, stock):
        if stock > 0:
            self.stock += stock
        else:
            raise VendingMachineError("１個以上補充してください")
