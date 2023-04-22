import matplotlib
import matplotlib.pyplot as plt

class Category:
    def __init__(self, s):
        self.category = s
        self.ledger = []

    def deposit(self, amt, desc=''):
        self.ledger.append({'amount': amt, 'description': desc})

    def withdraw(self, amt, desc=''):
        # funds = sum(filter(lambda x: x.get('amount') > 0, self.ledger))
        if self.check_funds(amt):
            self.ledger.append({'amount': -amt, 'description': desc})
            return True
        else:
            return False

    def get_balance(self):
        return sum([x.get('amount') for x in self.ledger])

    def transfer(self, amt, cat):
        # funds = sum(filter(lambda x: x.get('amount') > 0, self.ledger))
        if self.check_funds(amt):
            self.withdraw(amt, f'Transfer to {cat.category}')
            cat.deposit(amt, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amt):
        return self.get_balance() >= amt

    def __str__(self):
        bill = self.category.center(30, '*') + '\n'
        for i in self.ledger:
            bill += f'{i.get("description")[:23]:23}' + f'{i.get("amount"):7.2f}' + '\n'

        bill += f'Total: {self.get_balance():.2f}'
        return bill


def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    withdrawals = [-sum([i.get('amount') for i in cat.ledger if i.get('amount') < 0]) for cat in categories]
    percent_withdrawal = [round(i / sum(withdrawals) * 100) for i in withdrawals]
    names = [cat.category.lower().capitalize() for cat in categories]

    New_Colors = ['green','blue','purple']
    plt.bar(names, percent_withdrawal, color=New_Colors)
    plt.title(chart, fontsize=14)
    plt.xlabel('Category types', fontsize=14)
    plt.ylabel('Percentage of Total Withdrawals', fontsize=14)
    plt.grid(True)
    plt.show()


    return withdrawals





