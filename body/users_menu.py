#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

from body.users_database import *
from body.configured_logger import *

try:
    new_input = raw_input
except NameError:
    new_input = input


class EntryMenu(object):
    def __init__(self, username=None, position=None, operation=None):
        progress_logger.info('Starting users_menu.py')
        self.username = username
        self.position = position
        self.cmd_line_args = operation
        EntryMenu.choice_of_operation(self, operation)

    def choice_of_operation(self, operation):
        progress_logger.info("choice_of_operation Started")
        if operation is None:
            print_logger.info("What are you want to do?\n"
                  "1 : Log in | 2 : Sign Up | 3 : Quit")
            operation = str(new_input("To select an operation, enter the appropriate number: "))
        if operation == "1":
            EntryMenu.log_in(self)
            return self.username
        elif operation == "2":
            EntryMenu.registration(self)
        elif operation == "3":
            print_logger.info("Good bye")
            progress_logger.info("Session finished")
            quit()
        else:
            error_logger.error("Wrong input ({0})! Check the entered value and try again.".format(operation))
        progress_logger.info("choice_of_operation Finished")




    """Check database for user and load him"""

    def log_in(self):
        progress_logger.info("Autorization started")
        if self.username is None:
            self.username = new_input("Enter your username: ")
        db = DataBase(self.username, self.position, func='load_user')
        self.username, self.position, self.number_of_sales, self.total_value = \
            db.username, db.position, db.number_of_sales, db.total_value
        progress_logger.info("Authorization as {0} {1} completed".format(self.username, self.position))


    """Creating new user"""

    def registration(self):
        progress_logger.info("Registration started")
        if self.username is None:
            self.username = new_input("Enter your username: ")
        if self.position is None:
            while True:
                self.position = new_input("Enter your position: ")
                if self.position in ('Salesman', 'Manager'):
                    break
                else:
                    error_logger.error("Position of worker might be only"
                          " 'Salesman' or 'Manager'")
        DataBase(self.username, self.position, 'save_user')
        progress_logger.info("Registration completed")



if __name__ == '__main__':
    EntryMenu()
