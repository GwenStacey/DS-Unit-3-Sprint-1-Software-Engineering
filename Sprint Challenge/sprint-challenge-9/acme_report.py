#!/usr/bin/env python
'''Functions for generating products and reports'''

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        item = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        product = Product(item, 
                          price=randint(5, 100),
                          weight=randint(5, 100), 
                          flammability=uniform(0, 2.5))
        products.append(product)
    return products


def inventory_report(products):
    uniques = []
    weights = []
    prices = []
    flammabilities = []
    counter = 0
    for i in products:
        weights.append(i.weight)
        flammabilities.append(i.flammability)
        if (i not in uniques):
            prices.append(i.price)
            counter += 1
    mean_w = sum(weights)/len(weights)
    mean_p = sum(prices)/len(prices)
    mean_f = sum(flammabilities)/len(flammabilities)
    print(f'Number of unqiue items: {counter}')
    print(f'Mean weight:{mean_w}')
    print(f'Mean price:{mean_p}')
    print(f'Mean flammability{mean_f}')

if __name__ == '__main__':
    inventory_report(generate_products())