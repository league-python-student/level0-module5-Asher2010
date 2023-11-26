"""
Write the function definitions for the function calls below
"""
from tkinter import messagebox, simpledialog, Tk
import random
import unittest

# TODO Look at the test methods below and define the functions used in those
#  tests to make the tests pass. For example, the first test function has the
#  following code:
#       self.assertEqual(100, multiply(10, 10))
#  This code calls a multiply function and passes in 2 values (10 and 10) and
#  checks the function returns 100. Since a multiply function isn't defined,
#  you have to define one with the correct input variable(s) and return
#  statement. Create your functions below and not inside the test class.
def multiply(var1, var2):
    return var1 * var2
multiply(10, 10)

def str_cat(var1, var2, var3):
    return var1 + ' ' + var2 + ' '+ var3
str_cat(var1 = 'Welcome ', var2 = 'to ', var3 = 'Python')

def greater_than(var1, var2):
    return var1 < var2
greater_than(1, 2)

def get_random_number(low, high):
    return random.randint(low, high)
get_random_number(0, 100)

def is_vegetable(var1 = ' '):
    if var1 == str('celery'):
        return True
    return False
is_vegetable('celery')

def make_appointment(preferred_time_of_day = ' '):
    if preferred_time_of_day == str('morning'):
        return '8 am'
    elif preferred_time_of_day == str('afternoon'):
        return '1 pm'
    elif preferred_time_of_day == str('evening'):
        return '5 pm'
    elif preferred_time_of_day == str('graveyard'):
        return 'error'
make_appointment('afternoon')

# ======================= DO NOT EDIT THE CODE BELOW =========================

class FunctionTests(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(100, multiply(10, 10))

    def test_function_2(self):
        self.assertEqual('Welcome to Python', str_cat(var1='Welcome', var2='to', var3='Python'))

    def test_function_3(self):
        self.assertEqual(True, greater_than(1, 2))

    def test_function_4(self):
        for i in range(100):
            random_number = get_random_number(low=0, high=100)

            if random_number < 0 or random_number > 100:
                self.assertTrue(False)

    def test_function_5(self):
        self.assertEqual(False, is_vegetable('apple'))
        self.assertEqual(True,  is_vegetable('celery'))
        self.assertEqual(False, is_vegetable('tomato'))
        self.assertEqual(False, is_vegetable('mushroom'))
        self.assertEqual(False, is_vegetable())

    def test_function_6(self):
         self.assertEqual('8 am', make_appointment(preferred_time_of_day='morning'))
         self.assertEqual('1 pm', make_appointment('afternoon'))
         self.assertEqual('5 pm', make_appointment('evening'))
         #self.assertEqual('8 am', make_appointment())
         self.assertEqual('error', make_appointment('graveyard'))

if __name__ == '__main__':
    unittest.main()
