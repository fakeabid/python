class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance
    
    def __str__(self):
        return f'name: {self._name}\nbalance: {self._balance}\n'

class SavingsAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def calculate_interest(self):
        interest = self._balance * 0.05
        return interest
    
class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def calculate_interest(self):
        interest = self._balance * 0.02
        return interest
    
def main():
    ravi_acc = SavingsAccount("Ravi", 10000)
    anjali_acc = CurrentAccount('Anjali', 15000)

    print(f'{ravi_acc}interest: {ravi_acc.calculate_interest()}\n')
    print(f'{anjali_acc}interest: {anjali_acc.calculate_interest()}\n')
    print(f'total balance: {ravi_acc + anjali_acc}')

main()