slang = {'kicks': 'sneakers', 'whips': 'cars', 'flicks': 'movies'}
print(slang)

# lookup for key value instead of index
print slang['kicks']

# adding values
slang = {}
slang['celly'] = 'telephone'
slang['telly'] = 'hotel'
slang['food box'] = 'belly'
print slang

# updating values
slang['celly'] = 'phone'
print slang['celly']

# removing values
del slang['celly']
print slang

#look ups

#throws error, does not exist
#print slang['bloody']

# returns none, does not exist
r = slang.get('bloody')

if r:
    print r
else:
    print 'Not found'


# translate using dictionaries
slang = {'mate':'buddy', 'knackered':'tired', 'cheeky':'offensive'}
sentence = 'Sorry my mate is a bit cheeky'
translation = 'Sorry' + ' my ' + slang.get('mate') + ' is a bit ' + slang.get('cheeky')
print translation

# comparing lists & dictionaries

# note list must be ordered the same to match
my_list = [1, 2, 3, 4]
your_list = [1, 3, 2, 4]
her_list = [1, 2, 3, 4]

print (my_list == your_list)
print (my_list == her_list)

# dictionaries don't need to be ordered the same to match
my_list = { 1:1, 2:2, 3:3, 4:4 }
your_list = { 2:2, 3:3, 1:1, 4:4 }

print your_list == my_list

# a list of lists
menus = [['Bacon & Eggs', 'Cereal', 'French Toasts', 'Pancakes'],
        ['Soup', 'Salad', 'Roast Beef Sandwich', 'Hot Dog'],
        ['Steak', 'Fish', 'Burger']]

print 'Breakfast:\t', menus[0]
print 'Lunch:\t', menus[1]
print 'Dinner:\t', menus[2]

# getting a value from a 2D list
print 'Favorite Breakfast:\t', menus[0][0]

# a dictionary of lists
menus = {'Breakfast': ['Bacon & Eggs', 'Cereal', 'French Toasts', 'Pancakes'],
         'Lunch': ['Soup', 'Salad', 'Roast Beef Sandwich', 'Hot Dog'],
         'Dinner': ['Steak', 'Fish', 'Burger']
         }

# beast mode
print menus.get('Breakfast')[0]



