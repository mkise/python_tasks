# Define the menu and prices
menu = ['Porridge', 'British Breakfast', 'Greek Salad', 'Breakfast Burger']

price = {'Porridge':4.95,
         'British Breakfast':8.95,
         'Greek Salad':9.75,
         'Breakfast Burger':7.95
         }

# Print out the menu and prices
print(price)

# Define the stock for each menu item
stock = {'Porridge': 20,
         'British Breakfast':10 ,
         'Breakfast Burger':20 ,
         'Greek Salad': 5}

# Calculate the stock value for each item
stock_value = 0

for item in price:
    stock_value += price[item] * stock[item]


# Print out the stock value of each item
print(stock_value)
