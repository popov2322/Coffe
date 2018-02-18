#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

import os
from body.constants import *
from body.configured_logger import *

class Bill(object):
    users_directory = os.path.join(os.path.dirname(__name__), 'users')

    @staticmethod
    def save_last_bill(user, total_cost, add, beverage, cost_of_beverage, cost_of_add):
        progress_logger.info("Saving last bill...")
        """Checking/creating directory for bill"""
        if not os.path.exists(Bill.users_directory):
            os.makedirs(Bill.users_directory)
        file = os.path.join(os.path.dirname(__name__), 'users', '{}'.format(user))
        """Saving last bill"""
        with open(file, "w") as f:
            bill = LongPrints.BILL.format(beverage, cost_of_beverage, add, cost_of_add, total_cost, user)
            f.write(bill)
            print_logger.info("Last bill added")
        progress_logger.info("Last bill saved successfully")

    @staticmethod
    def load_last_bill(user):
        progress_logger.info("Loading last bill...")
        """Loading current user bill"""
        file = os.path.join(os.path.dirname(__name__), 'users', '{}'.format(user))
        try:
            with open(file, "r") as f:
                last_bill = f.read()
                print_logger.info(last_bill)
                progress_logger.info("Last bill loaded successfully")
        except IOError:
            error_logger.error("Last bill of {0} not found".format(user))
