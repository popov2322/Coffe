#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

from body.constants import *
from body.configured_logger import *
import sqlite3


class CoffeeShopDB(object):
    def __init__(self, item, item_cost=None):
        self.item = item
        self.item_cost = item_cost
        CoffeeShopDB.load_beverage(self, item)

    @staticmethod
    def create_db(connect, cursor):
        progress_logger.info("Cheking DB...")
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS coffee 
            (item TEXT, cost INTEGER)''')
        cursor.executemany("INSERT INTO coffee VALUES (?,?)", LongPrints.coffee_db_lines)
        connect.commit()
        progress_logger.info("DB exists")

    def load_beverage(self, item):
        progress_logger.info("Loading {}...".format(item))
        connect = sqlite3.connect(DBPath.db_file_path)
        cursor = connect.cursor()
        try:
            while True:
                try:
                    cursor.execute("SELECT cost FROM coffee WHERE item = ?", (self.item,))
                    data = cursor.fetchone()
                    self.item_cost = data[0]
                    progress_logger.info("{} loaded".format(item))
                    break
                except sqlite3.OperationalError:
                    CoffeeShopDB.create_db(connect, cursor)
        finally:
            cursor.close()
            connect.close()
