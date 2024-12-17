
class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Atributo de instacia
        Employee.total_employees += 1  # Atributo de class

    def show_total_employees():
        print(f"Total Employees: {Employee.total_employees}")

    def show(self):
        print(f'{self.name}: R${self.salary}')

    def __str__(self):
        return self.name


employee1 = Employee("Kebler Eulálio", 2000)
employee2 = Employee("João Nogueira", 1000)

# employee1.show_total_employees()
Employee.show_total_employees()

print('-'*50)
employee1.show()
employee2.show()

print('-'*50)
Employee.show(employee1)
Employee.show(employee2)


print('-'*50)
print(employee1)
print(employee2)
