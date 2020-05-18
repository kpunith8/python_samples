# https://www.youtube.com/watch?v=7lmCu8wz8ro
# https://github.com/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    # String representation of the class
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

p1 = Polynomial(1, 2, 4)
p2 = Polynomial(3, 1, 2)

# use -i option for interative way of accessing the data
# python -i python-tricks.py
# type p1 and p2 to get the __repr__ details

# Search for data models