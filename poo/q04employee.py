"""Classe com métodos de classe
Crie uma classe Employee com:
Atributos:
name e salary .
Um atributo de classe total_employees para contar quantos objetos da classe foram criados.
Métodos:
__init__() - inicializa o objeto e incrementa total_employees .
show_total_employees() - exibe o número total de funcionários.
Defina string de representação do objeto para ser o nome do funcionário.
"""
class Employee():
    total_employee = 0
    def __init__(self,name= '', salary = 0):
        self.name = name
        self.salary = salary #Atributo de instacia
        Employee.total_employee += 1 #Atributo de class

    def show_total_employees(self):
        print(f"Total Employees: {self.total_employee}")

    def __str__(self):
        return f'Employee: {self.name} \nSalary R${self.salary:.2f}'


fucionario1 = Employee("Kebler", 2000)
fucionario2 = Employee("João", 1000)

fucionario1.show_total_employees()

print(fucionario2)
print(fucionario1)



junir = Employee()
junir.name = junir
