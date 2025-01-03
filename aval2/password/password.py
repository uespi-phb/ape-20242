
class Password:

    def __init__(self, password):
        if not isinstance(password, (str, int)):
            raise TypeError(f'password must be an string or integer: {password}')
        
        self.value = str(password)


    def __str__(self):
        return self.mask()
    
    
    def __repr__(self):
        return f'Password({self.mask()})'
    

    def raw(self):
        return self.value
    

    def mask(self):
        passwd_len = len(self.value)
        if passwd_len == 0:
            return ''
        
        masked_len = passwd_len // 2 + 1
        if passwd_len >= 8:
            raw_len = 2
        elif passwd_len >= 5:
            raw_len = 1
        else:
            raw_len = 0

        mask_start = self.value[:raw_len]
        mask_end = self.value[-raw_len:] if raw_len > 0 else ''
        mask_middle = '*' * (passwd_len - 2 * raw_len)

        return f'{mask_start}{mask_middle}{mask_end}'


    def is_strong(self):
        if len(self.value) < 8:
            return False
        
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        for char in self.value:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            else:
                has_special = True

        return has_upper and has_lower and has_digit and has_special
