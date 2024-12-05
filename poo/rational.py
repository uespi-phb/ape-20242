
class Rational:
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den

    def __repr__(self):
        return f'Rational({self.num},{self.den})'

    def __str__(self):
        return f'{self.num}/{self.den}'

    def add(self, r):
        num = self.num * r.den + r.num * self.den
        den = self.den * r.den
        return Rational(num, den)

    def sub(self, r):
        num = self.num * r.den - r.num * self.den
        den = self.den * r.den
        return Rational(num, den)

    def mul(self, r):
        num = self.num * r.num
        den = self.den * r.den
        return Rational(num, den)

    def div(self, r):
        num = self.num * r.den
        den = self.den * r.num
        return Rational(num, den)


r1 = Rational(5, 3)
r2 = Rational(7)

print(r1.add(r2))
print(r1.sub(r2))
print(r1.mul(r2))
print(r1.div(r2))
