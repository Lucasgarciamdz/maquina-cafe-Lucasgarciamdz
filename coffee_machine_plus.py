class CoffeeMachinePlus:

    def __init__(self):
        self.resources = {
            'coin': 0,
            'coffee': 0,
            'sugar': 0,
            'milk': 0,
            'tea': 0,
            'chocolate': 0,
            'sugar': 0
        }

        self.recipies = {
            'simple_coffee': {
                'coffee': 30
            },
            'double_coffee': {
                'coffee': 60
            },
            'simple_milk_coffee': {
                'coffee': 15,
                'milk': 15
            },
            'double_milk_coffee': {
                'coffee': 30,
                'milk': 30
            },
            'tea': {
                'tea': 15
            },
            'chocolate': {
                'chocolate': 20
            },
            'milk_chocolate': {
                'chocolate': 10,
                'milk': 10
            }
        }

    def insert_coin(self):
        self.resources['coin'] += 1

    def refill(self, type, amount):
        self.resources[type] += amount

    def get_product(self, product_type, sugar_level):
        sugar = 3 * sugar_level
        self.check_resources(product_type)
        if self.resources['sugar'] < sugar:
            return False
        self.resources['coin'] -= 1
        self.resources['sugar'] -= sugar
        return True

    def check_resources(self, product_type):
        recipie = self.recipies[product_type]
        for resource in recipie:
            if self.resources[resource] < recipie[resource]:
                return False
        if self.resources['coin'] == 0:
            return False
        return True
