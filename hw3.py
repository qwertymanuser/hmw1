class Bank:
    def __init__(self, _name) -> None:
        self._name = _name
        self._balance = 0
    def money_x(self):
        user = int(input("сколько вы хотите пополнить баланс: "))
        self._balance += user
        return f"на вашем счете: {self._balance}, Имя владельца: {self._name}"
    def kill(self):
        user = int(input("сколько вы хотите обноличить: "))
        if self._balance >= user:
            self._balance -= user
            return f"вы обноличили счет на{user} остаток на карте {self._balance}"
        else:
            return f"На вашем счете недостаточно средств: {self._balance}"
    def jackpot(self):
        return f"ваш счет умножен на 10, ваш счет: {self._balance} * 10"
    def user(self, name, _balanse):
        self.name = name
        self._balanse = _balanse
        return f"Имя: {self.name}, Balanse: {self._balanse + self._balance}"
ban = Bank("mar")
print(ban.money_x())
print(ban.kill())
