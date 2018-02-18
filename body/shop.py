#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

from body.shop_database import *
from body.constants import *
from body.users_database import *
from body.bill import *

try:
    new_input = raw_input
except NameError:
    new_input = input

class CoffeeShop(object):
    def __init__(self, user, beverage=None, cost_beverage=0, add=None, cost_add=0):
        self.beverage = beverage
        self.add = add
        self.cost_beverage = cost_beverage
        self.cost_add = cost_add
        CoffeeShop.menu(self, item=beverage, type_of_item="beverage")
        CoffeeShop.menu(self, item=add, type_of_item="add")
        Bill.save_last_bill(user=user.username, beverage=self.beverage, cost_of_beverage=self.cost_beverage,
                                      add=self.add, cost_of_add=self.cost_add, total_cost=self.total_cost)
        DataBase.refresh_user(username=user.username, value=self.total_cost)
        progress_logger.info("CoffeeShop completed")

    def menu(self, item, type_of_item):
        if item is None:
            item = CoffeeShop.input_item(type_of_item)
        data = CoffeeShopDB(item)
        if type_of_item == "add":
            self.add, self.cost_add = item, data.item_cost
        if type_of_item == "beverage":
            self.beverage, self.cost_beverage = item, data.item_cost
        self.total_cost = self.cost_add + self.cost_beverage

    @staticmethod
    def input_item(type_of_item):
        if type_of_item == "add":
            printer_text = LongPrints.ADDS_PRINT
            input_text = LongPrints.ADDS_INPUT
            list_of_choices = HelpsAndChoices.ADDS_CHOICES
        else:
            printer_text = LongPrints.COFFEE_PRINT
            input_text = LongPrints.COFFEE_INPUT
            list_of_choices = HelpsAndChoices.BEVERAGE_CHOICES
        print_logger.info(printer_text)
        while True:
            item = new_input(input_text)
            if item in list_of_choices:
                break
            error_logger.error("{} wrong input! Please check your input and try again.".format(item))
        return item