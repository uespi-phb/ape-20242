
from random import randint
from donor import Donor



def main():
    blood_types = ('A', 'B', 'AB', 'O')
    rh_factors = ('+', '-')
    donors = []

    for type in blood_types:
        for rh in rh_factors:
            blood_type = f'{type}{rh}'
            name = f'Donor {blood_type}'
            age = randint(16, 60)
            donors.append(Donor(name, age, blood_type))

    for donor in donors:
        for other in donors:
            can_donate = donor.can_donate_to(other)
            print(f'{str(donor):<18} ==> {str(other):<18}: {can_donate}')


if __name__ == '__main__':
    main()
