#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

import os


class HelpsAndChoices:
    DESCRIPTION = "Commandline utility that will be used by salesmen and manages of the “CoffeeForMe” company"
    BEVERAGE_CHOICES = ["water", "espresso", "latte", "cappuccino", "tea", "americano"]
    ADDS_CHOICES = ["zest", "sugar", "syrup", "cane_sugar", "cinnamon", "none"]
    CMD_HELP = "Use this option if you want prefer commandline mode"
    USERNAME_HELP = "input your username after this key"
    POSITION_HELP = "input your work position after this key"
    ADD_USER_HELP = "Use this option if you want to add new user"
    ACTION_HELP = "1:sell a drink(salesman)\n2:Get the beverage price(Salesman)\n" \
                  "3:Load last bill(Salesman)\n4:Show sales records(Manager)\n5:Exit"
    BEVERAGE_HELP = "Select beverage type"
    ADDS_HELP = "Select additional(enter none if u don't want additional)"


class LongPrints:
    ACTION_LONG_PRINT = "Operations: \n{0}{1:>15}{2}\n{3}{1:>5}{2}\n{4}{1:>13}{2}\n{5}{1:>9}{6}\n{7}".format(
        "1:Sell a drink", "|", "(only for salesmans)", "2:Get the beverage price",
        "3:Load last bill", "4:Show sales records",
        "(only for managers)", "5:Exit")
    COFFEE_PRINT = ("Beverages menu:\n"
                    "{1}{0:^10}{2:>1}\n{3}{0:^6}{4:>6}\n{5}{0:^8}{6:>6}"
                    .format("|", "espresso", "latte", "cappuccino", "tea", "americano", "water"))
    ADDS_PRINT = ("Are u need additional? \n"
                  "{1:>4}{0:^17}{2:>6}\n{3}{0:^15}{4}\n{5}{0:^10}{6:>8}"
                  .format("|", "zest", 'sugar', "syrup", "cane sugar", "cinnamon", "none"))
    COFFEE_INPUT = "Enter type of coffee here: "
    ADDS_INPUT = "Enter additional:"
    COFFEE_LIST = ["espresso", "latte", "cappuccino", "tea", "americano"]
    ADDS_LIST = ["zest", "sugar", "syrup", "cane sugar", "cinnamon", "none"]
    BILL = "------------------------------------\n" \
           "Thank you for buying at CoffeeForMe:\n" \
           "{0}:{1}\n" \
           "{2}:{3}\n" \
           "Total cost: {4}\n" \
           "You were served by {5}\n" \
           "Have a nice day!\n" \
           "------------------------------------"
    coffee_db_lines = [("espresso", 15), ("latte", 30), ("cappuccino", 25), ("tea", 20), ("americano", 20),
                       ("water", 5), ("zest", 1), ('sugar', 1), ("syrup", 3), ("cane sugar", 2), ("cinnamon", 2),
                       ("none", 0)]


class DBPath:
    db_path = os.path.join(os.path.dirname(__name__), "database")
    db_file_path = os.path.join(os.path.dirname(__name__), "database", "my.sqlite")
