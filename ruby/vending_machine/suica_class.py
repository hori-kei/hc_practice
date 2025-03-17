from exception import VendingMachineError


class Suica:
    # Suicaクラスのインスタンス変数でデフォで500円チャージされた変数を作成
    # インスタンス変数はself.__balanceで外部から残高変更できないように見せる
    def __init__(self):
        self.__balance = 500

    # depositメソッドで、100円以上のチャージができるようにする、100円以下は例外発生

    def withdraw(self, price):
        if self.__balance > price:
            self.__balance -= price
        else:
            raise VendingMachineError("お金が足りません")

    # 現在の残高を取得できるcurrent_balanceメソッド作成
    # propertyメソッドでインスタンス.balanceで残高を表示できるようにする
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, price):
        if price >= 100:
            self.__balance += price
        else:
            raise VendingMachineError("100円以上のチャージをしてください")
