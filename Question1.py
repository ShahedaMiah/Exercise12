
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# This adds each character of the string as a separate list item
cheese += 'Oke'
print(cheese)

# Extending the list by multiple items through creating a new list and extending the original using those new values
new_items = ['Mozzarella', 'Halloumi']
cheese.extend(new_items)
print(cheese)

