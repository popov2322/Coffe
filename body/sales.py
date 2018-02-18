#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov DA"

import sqlite3
from body.constants import *
from body.configured_logger import *

class Sales:
    def __init__(self):
        db_data = Sales.get_db_data()
        Sales.data_printer(data=db_data)

    @staticmethod
    def get_db_data():
        connect = sqlite3.connect(DBPath.db_file_path)
        cursor = connect.cursor()
        cursor.execute("SELECT name, number_of_sales, total_value FROM users WHERE position = 'Salesman'")
        return cursor.fetchall()


    @staticmethod
    def data_printer(data):
        full_total_value = 0
        full_number_of_sales = 0
        print_logger.info("Seller name         |   Number of sales  |  Total Value(c.u.)")
        for string in data:
            name, number_of_sales, total_value = string[0], string[1], string[2]
            print_logger.info("{1:^20}{0}{2:^20}{0}{3:^20}".format("|",name, number_of_sales, total_value))
            full_total_value += total_value
            full_number_of_sales += number_of_sales
        print_logger.info("{1:^20}{0}{2:^20}{0}{3:^20}".format("|", "Total:", full_number_of_sales, full_total_value))
