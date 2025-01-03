
from random import randint
from password_manager import PasswordManager

def main():
    manager = PasswordManager()

    print(f'{"SENHA":<15} {"MÁSCARA":<15} FORTE')
    for k in range(10):
        password_length = randint(1, 15)
        password = manager.generate_password(password_length)
        strong = 'Sim' if manager.validate_password(password) else 'Não'
        print(f'{password.raw():<15} {str(password):<15} {strong}')


if __name__ == '__main__':
    main()
