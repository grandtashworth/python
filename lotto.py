#!/home/grandt/PycharmProjects/Lotto/venv/bin/python

"""
__name__ = "Lucky Lotto Numbers"
__author__ = "Grandt Ashworth"
__date__ = "26 August 2020"
__version__ = "1.0"
"""

import random

uk_lotto_number_pick_count = 6
uk_lotto_number_last_number = 59
my_uk_lotto_numbers = []
eu_lotto_number_pick_count = 5
eu_lotto_lucky_number_pick_count = 2
eu_lotto_number_last_number = 50
eu_lotto_lucky_last_number = 12
my_eu_lotto_numbers = []
my_eu_lotto_lucky_numbers = []

while uk_lotto_number_pick_count != 0:
    my_uk_lotto_number = random.randint(1, uk_lotto_number_last_number)
    if my_uk_lotto_number not in my_uk_lotto_numbers:
        my_uk_lotto_numbers.append(my_uk_lotto_number)
        uk_lotto_number_pick_count = uk_lotto_number_pick_count - 1

while eu_lotto_number_pick_count != 0:
    my_eu_lotto_number = random.randint(1, eu_lotto_number_last_number)
    if my_eu_lotto_number not in my_eu_lotto_numbers:
        my_eu_lotto_numbers.append(my_eu_lotto_number)
        eu_lotto_number_pick_count = eu_lotto_number_pick_count - 1

while eu_lotto_lucky_number_pick_count != 0:
    my_eu_lotto_lucky_number = random.randint(1, eu_lotto_lucky_last_number)
    if my_eu_lotto_lucky_number not in my_eu_lotto_lucky_numbers:
        my_eu_lotto_lucky_numbers.append(my_eu_lotto_lucky_number)
        eu_lotto_lucky_number_pick_count = eu_lotto_lucky_number_pick_count - 1

print("")
print(">>> Here Are your Winning Numbers:")
print("UK Lotto Numbers: %s" % my_uk_lotto_numbers)
print("EU Lotto Numbers: %s with Lucky Numbers: %s" % (my_eu_lotto_numbers, my_eu_lotto_lucky_numbers))
print("")
