import unittest

from coffee_machine_plus import CoffeeMachinePlus


class TestCoffeeMachine_plus(unittest.TestCase):

    def setUp(self) -> None:
        self.machine = CoffeeMachinePlus()

    def test_no_coin(self):
        self.assertFalse(self.machine.get_product('simple_coffee', 0))

    def test_insert_coin(self):
        self.machine.insert_coin()
        self.assertEqual(self.machine.resources['coin'], 1)

    def test_refill_0(self):
        self.machine.refill('coffee', 0)
        self.machine.refill('sugar', 0)
        self.machine.refill('milk', 0)
        self.machine.refill('chocolate', 0)
        self.machine.refill('tea', 0)
        self.assertEqual(self.machine.resources['sugar'], 0)
        self.assertEqual(self.machine.resources['coffee'], 0)
        self.assertEqual(self.machine.resources['milk'], 0)
        self.assertEqual(self.machine.resources['chocolate'], 0)
        self.assertEqual(self.machine.resources['tea'], 0)

    def test_refill_10(self):
        self.machine.refill('coffee', 10)
        self.machine.refill('sugar', 10)
        self.machine.refill('milk', 10)
        self.machine.refill('chocolate', 10)
        self.machine.refill('tea', 10)
        self.assertEqual(self.machine.resources['sugar'], 10)
        self.assertEqual(self.machine.resources['coffee'], 10)
        self.assertEqual(self.machine.resources['milk'], 10)
        self.assertEqual(self.machine.resources['chocolate'], 10)
        self.assertEqual(self.machine.resources['tea'], 10)

    def test_get_simple_coffee_1(self):
        self.machine.refill('coffee', 30)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('simple_coffee', 0))
        self.assertEqual(self.machine.resources['coffee'], 30 - 30)
        self.assertEqual(self.machine.resources['coin'], 0)

    def test_get_double_coffee_1(self):
        self.machine.refill('coffee', 60)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('double_coffee', 0))
        self.assertEqual(
            self.machine.resources['coffee'],
            60 - (self.machine.recipies['double_coffee']['coffee']))
        self.assertEqual(self.machine.resources['coin'], 0)

    def test_get_simple_milk_coffee_1(self):
        self.machine.refill('coffee', 30)
        self.machine.refill('milk', 30)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('simple_milk_coffee', 0))
        self.assertEqual(
            self.machine.resources['coffee'],
            30 - (self.machine.recipies['simple_milk_coffee']['coffee']))
        self.assertEqual(
            self.machine.resources['milk'],
            30 - (self.machine.recipies['simple_milk_coffee']['milk']))
        self.assertEqual(self.machine.resources['coin'], 0)

    def test_get_double_milk_coffee_1(self):
        self.machine.refill('coffee', 30)
        self.machine.refill('milk', 30)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('double_milk_coffee', 0))
        self.assertEqual(
            self.machine.resources['coffee'],
            30 - (self.machine.recipies['double_milk_coffee']['coffee']))
        self.assertEqual(
            self.machine.resources['milk'],
            30 - (self.machine.recipies['double_milk_coffee']['milk']))
        self.assertEqual(self.machine.resources['coin'], 0)

    def test_get_tea(self):
        self.machine.refill('tea', 20)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('tea', 0))
        self.assertEqual(self.machine.resources['coin'], 0)
        self.assertEqual(self.machine.resources['tea'],
                         20 - self.machine.recipies['tea']['tea'])

    def test_get_chocolate(self):
        self.machine.refill('chocolate', 20)
        self.machine.insert_coin()
        self.assertTrue(self.machine.get_product('chocolate', 0))
        self.assertEqual(self.machine.resources['coin'], 0)
        self.assertEqual(self.machine.resources['chocolate'],
                         20 - self.machine.recipies['chocolate']['chocolate'])

    def test_sugar(self):
        self.machine.refill('sugar', 30)
        self.machine.insert_coin()
        self.assertFalse(self.machine.get_product('simple_coffee', 3))

    def test_low_sugar(self):
        self.machine.refill('sugar', 1)
        self.machine.insert_coin()
        self.assertFalse(self.machine.get_product('simple_coffee', 1))

    def test_0_coins(self):
        self.machine.refill('sugar', 30)
        self.machine.refill('coffee', 30)
        self.assertFalse(self.machine.get_product('simple_coffee', 1))

    def test_no_sugar(self):
        self.machine.refill('sugar', 0)
        self.machine.insert_coin()
        self.machine.refill('coffee', 30)
        self.assertFalse(self.machine.get_product('simple_coffee', 1))

    def test_no_milk(self):
        self.machine.refill('milk', 0)
        self.machine.insert_coin()
        self.assertFalse(self.machine.get_product('simple_milk_coffee', 1))

    def test_no_coffee(self):
        self.machine.refill('coffee', 0)
        self.machine.insert_coin()
        self.assertFalse(self.machine.get_product('simple_coffee', 1))

    def test_no_tea(self):
        self.machine.refill('tea', 0)
        self.machine.insert_coin()
        self.assertFalse(self.machine.get_product('tea', 1))


if __name__ == "__main__":
    unittest.main()
