"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self

    def add_stock(self, amount):
        self.qty += amount

    def sell(self, amount):
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        else:
            if self.qty - amount < 0:
                self.qty = 0
            else:
                self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
        amt_of_ingredients = []
        for i in ingredients:
            amt_of_ingredients.append((i[0], amount * i[1]))
        return amt_of_ingredients


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    @classmethod
    def get(cls, name):
        if name not in cls.cache:
            print('Sorry, that cupcake doesn\'t exist')
            return

        return cls.cache[name]

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
