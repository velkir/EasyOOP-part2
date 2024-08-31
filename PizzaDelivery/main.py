import operator

class PizzaDelivery:
    def __init__(self, name, price, ingredients=None, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients if ingredients else {}
        self.ordered = ordered

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            print("A pizza is already ordered, it can't be modified")
        else:
            ingredient_value = self.ingredients.get(ingredient)
            if ingredient_value:
                ingredient_value += quantity
            else:
                ingredient_value = quantity
            self.ingredients[ingredient] = ingredient_value
            self.price += quantity * price_per_ingredient
            print(f"Ingredient added. New price: {self.price}")


    def remove_ingredient(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            print("A pizza is already ordered, it can't be modified")
        else:
            ingredient_value = self.ingredients.get(ingredient)
            if ingredient_value:
                if ingredient_value >= quantity:
                    self.ingredients[ingredient] -= quantity
                    self.price -= quantity * price_per_ingredient
                    print(f"Ingredient removed. New price: {self.price}")
                else:
                    print("Quantity to remove is too large.")
            else:
                print("Incorrect ingredient")

    def make_order(self):
        self.ordered = True
        return (f"Name: {self.name}\n"
                f"Price: {self.price}\n"
                f"Ingredients:\n"
                f"{'\n'.join([f'{ingredient}: {quantity}' for ingredient, quantity in self.ingredients.items()])}")

pepperoni = PizzaDelivery("Pepperoni", 10)
pepperoni.add_extra("meat", 3, 1)
pepperoni.add_extra("goat cheese", 1, 2)
pepperoni.add_extra("salad", 1, 1)

pepperoni.remove_ingredient("meat", 1, 1)
print()
print(pepperoni.make_order())
pepperoni.add_extra("salad", 1, 1)
pepperoni.remove_ingredient("meat", 1, 1)
