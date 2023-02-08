book_price = 24.95
discount = .60
shipping_price_rest = .75
shipping_price_first = 3.00
total_units = 60

book_discount_amount = book_price * discount * total_units
shipping = shipping_price_rest * (total_units - 1) + shipping_price_first

result = book_discount_amount + shipping

print(""" The total price for {0:d} books including shipping and discount is:
		Total price of the books is: {1:7.2f}
		Total shipping is:           {2:7.2f}
		Total price is:              {3:7.2f}""".format(total_units, book_discount_amount, shipping, result))