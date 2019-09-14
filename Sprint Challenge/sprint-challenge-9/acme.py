import random

'''Creating a class to represent the basics of a product
with the acme corporation'''


class Product():

    '''Basic product class'''
    def __init__(self,
                 name='Product',
                 price=10,
                 weight=20,
                 flammability=0.5,
                 identifier=random.uniform(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def Stealability(self):
        '''Determine if an item is worth stealing'''
        stealability = self.price/self.weight
        if stealability < 0.5:
            print('Not so stealable...')
        elif(stealability >= 0.5 and stealability < 1.0):
            print('Kinda stealable.')
        else:
            print('Very stealable')
        return stealability

    def Explode(self):
        power = self.flammability*self.weight
        if(power < 10):
            print('Fizzle')
        elif(power >= 10 and power < 50):
            print('...boom!')
        else:
            print('...BABOOM!!')
        return power


class BoxingGlove(Product):

    def __init__(self,
                 name,
                 price=10,
                 weight=10,
                 flammability=0.5):
        super().__init__(self, 
                         name,
                         weight,
                         price,
                         flammability)

    def Explode(self):
        print("...it's a glove")