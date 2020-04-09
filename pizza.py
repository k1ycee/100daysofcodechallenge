toppings = ["pepperoni", "pineapple", "chesse", "sausage", "olives", "anchovies", "mushrooms"]

price = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell "+str(num_pizzas)+" different kinds of pizza")

pizzas = list(zip(price, toppings))
print(list(pizzas))
pizzas.sort()
# print(pizzas)
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(list(three_cheapest))

num_two_dollar_slices = price.count(2)
# print(list(str(num_two_dollar_slices)))