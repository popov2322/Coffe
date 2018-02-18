#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

import sqlite3
import os
from body.constants import *
from body.configured_logger import *


class DataBase(object):

    def __init__(self, username, position, func):
        self.username = username
        self.position = position
        if not os.path.exists(DBPath.db_path):
            os.makedirs(DBPath.db_path)
            progress_logger.info("directory for db created")
        getattr(DataBase, func)(self)

    '''CREATING TABLE IF NOT EXISTS'''

    @staticmethod
    def create_db(cursor):
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users 
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT,
            position TEXT, number_of_sales INTEGER, total_value INTEGER)''')

    '''Checking user in DB'''

    @staticmethod
    def check_db_for_user(name):
        connect = sqlite3.connect(DBPath.db_file_path)
        # Создание курсора
        cursor = connect.cursor()
        cursor.execute("SELECT rowid FROM users WHERE name = ?", (name,))
        data = cursor.fetchone()
        if not data is None:
            progress_logger.info("User exists")
            return True
        else:
            progress_logger.info("User not exists")
            return False

    '''Creating new user in DB'''

    def save_user(self):
        progress_logger.info("Creating new user in DB...")
        connect = sqlite3.connect(DBPath.db_file_path)
        # Создание курсора
        cursor = connect.cursor()
        DataBase.create_db(cursor)
        check = DataBase.check_db_for_user(self.username)
        try:
            if not check:
                '''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name TEXT,
                             position TEXT, number_of_sales INTEGER, total_value INTEGER)'''
                # Наполнение таблицы
                cursor.execute(
                    "INSERT INTO users (name,position,number_of_sales, total_value) VALUES ('{0}','{1}','{3}','{3}')"
                        .format(self.username, self.position, 0, 0))
                # Подтверждение отправки данных в базу
                connect.commit()
                print_logger.info("{1} {0} successfully created".format(self.username, self.position))
                progress_logger.info("{1} {0} successfully created".format(self.username, self.position))
            else:
                error_logger.error("'{0}' aready in program u need to use another name.".format(self.username))
            quit()
        # Завершение соединения
        finally:
            cursor.close()
            connect.close()

    '''Loading user from DB'''

    def load_user(self):
        progress_logger.info("Loading user from DB...")
        connect = sqlite3.connect(DBPath.db_file_path)
        cursor = connect.cursor()
        DataBase.create_db(cursor)
        check = DataBase.check_db_for_user(self.username)
        try:
            if check:
                cursor.execute("SELECT name, position, number_of_sales, total_value FROM users WHERE name = ?",
                               (self.username,))
                data = cursor.fetchone()
                self.username, self.position, self.number_of_sales, self.total_value = data
                progress_logger.info("{0} {1} loaded successfully".format(self.username, self.position))
            else:
                error_logger.error("User {0} is not exists.".format(self.username))
                quit()
        finally:
            cursor.close()
            connect.close()

    '''Обновление количества продаж и итоговой суммы'''

    @staticmethod
    def refresh_user(value, username):
        progress_logger.info("Refreshing sales data of {0}...".format(username))
        connect = sqlite3.connect(DBPath.db_file_path)
        cursor = connect.cursor()
        try:
            cursor.execute(
                "UPDATE users SET number_of_sales=number_of_sales + 1, total_value=total_value + ? WHERE name=?",
                (value, username))
            connect.commit()
            progress_logger.info("Users data refreshed")
        finally:
            cursor.close()
            connect.close()
