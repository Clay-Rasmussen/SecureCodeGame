'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_PAYABLE = Decimal('1000000.00')

def validorder(order: Order):
    net = Decimal('0')
    total_payable = Decimal('0')

    for item in order.items:
        # Convert amount and quantity to Decimal via string conversion to avoid float precision loss
        amount = Decimal(str(item.amount))
        quantity = Decimal(str(item.quantity))

        if item.type == 'payment':
            net += amount
        elif item.type == 'product':
            item_total = amount * quantity
            net -= item_total
            total_payable += item_total
        else:
            return "Invalid item type: %s" % item.type

    # Check for order amount limit
    if total_payable > MAX_PAYABLE:
        return "Total amount payable for an order exceeded"

    if net != Decimal('0'):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id