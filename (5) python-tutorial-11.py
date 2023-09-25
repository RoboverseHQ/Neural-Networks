# Section 11. Modules & Packages

# Writing Python modules

# Importing module objects

#1) import <module_name>

# main.py
import pricing


net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

# 2) import <module_name> as new_name

import pricing as selling_price

net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

# 3) from <module_name> import <name>

from module_name import fn1, fn2

fn1()
fn2()

# main.py
from pricing import get_net_price

# main.py
from pricing import get_net_price

net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)

# 4) from <module_name> import <name> as <new_name>: rename the imported objects
#from <module_name> import <name> as <new_name>

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)

# 5) from <module_name> import * : import all objects from a module

from module_name import *

# product.py
def get_tax(price):
    return price * 0.1

from pricing import *
from product import *

tax = get_tax(100)
print(tax)

# Introduction to Python module search path
import sys

for path in sys.path:
    print(path)


'''
>>> import sys
>>> sys.path.append('d:\\modules\\')
>>> import recruitment
>>> recruitment.hire()
Hire a new employee...
'''

# Python __name__

if __name__ == '__main__':
    main()
    
    
    def calculate_tax(price, tax):
        return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)

if __name__ == '__main__':
    print_billing_doc()
    


# Python Packages
import package.module

package.module.function

# main.py
import sales.order
import sales.delivery
import sales.billing


sales.order.create_sales_order()
sales.delivery.create_delivery()
sales.billing.create_billing()

# main.py
from sales.order import create_sales_order
from sales.delivery import create_delivery
from sales.billing import create_billing


create_sales_order()
create_delivery()
create_billing()


# main.py
from sales.order import create_sales_order as create_order
from sales.delivery import create_delivery as start_delivery
from sales.billing import create_billing as issue_billing


create_order()
start_delivery()
issue_billing()


# Initializing a package

# main.py
from sales import TAX_RATE

print(TAX_RATE)


# __init__.py

# import the order module automatically
from sales.order import create_sales_order

# default sales tax rate
TAX_RATE = 0.07



# main.py
import sales

sales.order.create_sales_order()



# main.py
from sales import *


order.create_sales_order()
delivery.create_delivery()

# cannot access the billing module


# Subpackages

# main.py
from sales.order import create_sales_order

create_sales_order()