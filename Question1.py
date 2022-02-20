
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# This adds each character of the string as a separate list item
cheese += 'Oke'
print(cheese)

# Extending the list by multiple items through creating a new list and extending the original using those new values
new_items = ['Mozzarella', 'Halloumi']
cheese.extend(new_items)
print(cheese)

#Mya
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# print(cheese)
# result is ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']
# adds each character in 'oke' as separate items in the list
cheese.append('Oke')
# '.append()' adds to the end of the list. you can only have 1 argument with .append()
print(cheese)

cheese.insert(4, 'Brie')
# 'insert(4, 'Oke') inserts in the 4th element(starting from 0)
print(cheese)

cheese.extend(['Jarlsberg', 'Comet'])
# you can only have 1 argument with .extend(), but you can get around it by putting more than 1 argument into a list
print(cheese)