total = 0
prices = [1.50, 39.99, 60.00]

# iterating and printing
for price in prices:
    print 'price: ', price
    total += price
    print 'total prices: ', total

# finding the average
average = total/len(prices)
print 'Average price: ', average