#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

from body.users_database import *
from body.constants import *
from body.bill import *
from body.sales import *
from body.shop_database import *
from body.shop import *

try:
    new_input = raw_input
except NameError:
    new_input = input


class ActionMenu(object):
    def __init__(self, user, action=None, beverage=None, add=None, total_cost=None):
        self.user = user
        self.beverage = beverage
        self.add = add
        self.total_cost = total_cost
        print_logger.info("\nHello {0} {1}!\n".format(user.position, user.username))
        ActionMenu.menu(self, action=action)

    def menu(self, action):
        number_of_operation = action
        if action is None:
            print_logger.info(LongPrints.ACTION_LONG_PRINT)
            number_of_operation = new_input("Select the operation you want to execute: ")

        if number_of_operation == "1":
            if not self.user.position == "Salesman":
                error_logger.error("Premission denied")
            else:
                progress_logger.info("CoffeeShop started...")
                sell = CoffeeShop(self.user, beverage=self.beverage, add=self.add)

        elif number_of_operation == "2":
            if not self.user.position == "Salesman":
                error_logger.error("Permission denied")
            else:
                if self.beverage is None:
                    beverage = CoffeeShop.input_item("beverage")
                else:
                    beverage = self.beverage
                progress_logger.info("Cheking cost of {}".format(beverage))
                data = CoffeeShopDB(beverage)
                print_logger.info("Price of {0} is {1}(c.u.)".format(beverage, data.item_cost))
                progress_logger.info("Price of {0} loaded".format(beverage))

        elif number_of_operation == "3":
            if not self.user.position == "Salesman":
                error_logger.error("Permission denied")
            else:
                bill = Bill.load_last_bill(self.user.username)

        elif number_of_operation == "4":
            if not self.user.position == "Manager":
                error_logger.error("Permission denied")
            else:
                Sales()
        elif number_of_operation == "5":
            progress_logger.info("Session finished")
            print_logger.info("Good bye {}".format(self.user.username))
            quit()

        else:
            error_logger.error("Wrong input ({0})! Check the entered value and try again.".format(number_of_operation))
        if new_input("Press 'y' to continue in interactive mode, or any key to exit: ") == "y":
            ActionMenu.menu(self, action=None)
        else:
            ActionMenu.menu(self, action="5")
