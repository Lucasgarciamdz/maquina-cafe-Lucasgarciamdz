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
            },
            'double_chocolate': {
                'chocolate': 40,
            },
        }

    def insert_coin(self):
        self.resources['coin'] += 1

    def refill(self, type, amount):
        self.resources[type] += amount

    def get_product(self, product_type, sugar_level):
        if self.check_resources(product_type, sugar_level):
            recipie = self.recipies[product_type]
            for resource in recipie:
                self.resources[resource] -= recipie[resource]
            self.resources['coin'] -= 1
            self.resources['sugar'] -= sugar_level * 3
            return True

    def check_resources(self, product_type, sugar_level):
        recipie = self.recipies[product_type]
        sugar_level = 3 * sugar_level
        for resource in recipie:
            if self.resources[resource] < recipie[resource]:
                return False
        if self.resources['coin'] == 0 or self.resources['sugar'] < sugar_level:
            return False
        return True
