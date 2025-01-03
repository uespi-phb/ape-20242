
from random import choice
from password import Password


class PasswordManager:

    def __init__(self):
        # String of chars with ASCII codes between 33 (!) and 126 (~)
        self.valid_chars = ''
        for code in range(33, 127):
            self.valid_chars += chr(code)


    def generate_password(self, length):
        if length <= 0:
            raise ValueError(f'Invalid password length: {length}')

        password = ''
        for _ in range(length):
            password += choice(self.valid_chars)

        return Password(password)


    def validate_password(self, password):
        if not isinstance(password, Password):
            raise TypeError('password must be instance of Password')
        
        return password.is_strong()
    
