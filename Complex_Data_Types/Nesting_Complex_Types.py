
# Dictionarys
stock_qty = {

}

# stock_qty['Banana'] = 50
# stock_qty['Apple'] = 150
# stock_qty['Pear'] = 86

#print("\nstock quantities: ",stock_qty)

#stock_qty['Avacado'] = 77
#stock_qty['Pineapple'] = 37

#print("\nstock quantities: ",stock_qty)


stock_consumed = {'Banana': [77, 105, 298, 321],
                  'Apple': [50, 100, 77, 62],
                  'Pear': [33, 67, 88, 11],
                  'Avacado': [105, 32, 44, 71],
                  'Pineapple': [12, 89, 100, 4]}

print("\nstock quantities consumed: ", stock_consumed)
# Lookup by key - returns list
print("\nStock consumed", stock_consumed['Pear'])
print("\nStock consumed by index", stock_consumed['Pear'][1])


daily_stock_consumed = { # Dict in a Dict
'banana' : { 'fri' : 70, 'Sat' : 50, 'Sun' : 23 },
'pear' : {'fri' : 54, 'Sat' : 47, 'Sun' : 22}
}
print("\nWhat was consumed on a given day: ",daily_stock_consumed['banana']['Sat'])# Nested lookup


