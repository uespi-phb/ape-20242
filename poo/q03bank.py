"""Classe com validações
Crie uma classe BankAccount com:
Atributos:
holder (nome do titular, fornecido no construtor).
balance (valor inicial, padrão 0).
Métodos:
deposit(amount) - adiciona ao saldo.
withdraw(amount) - reduz o saldo (somente se houver saldo suficiente).
print_balance() - exibe o saldo atual.
Defina o formato da string de representação do objeto para: BankAccount(Fulano de Tal; R$197,53) , onde Fulano de Tal é o nome do cliente
e R$0,00 o saldo.
"""

import utils


class BankAccount:
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0.00

    def deposit(self, amount):
        if amount < 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if (amount < 0) or (self.balance < amount):
            return False
        self.balance -= amount
        return True

    def print_balance(self):
        print('BANCO EXEMPLO S/A')
        print('SALDO DA CONTA')
        print('Titular:', self.holder)
        print('Saldo  :', utils.float_to_currency(self.balance))

    def __repr__(self):
        return str(self)

    def __str__(self):
        currency = utils.float_to_currency(self.balance)
        return f'BankAccount({self.holder}; {currency})'


a1 = BankAccount('Fulano de Tal')
a1.deposit(5125.93)
a1.withdraw(200.00)
a1.print_balance()