#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

"""Лаунчер CoffeeForMe"""

from body import *


def entry():
    cmd_args = get_args()
    if not cmd_args.cmd:
        progress_logger.info("Programm started in interactive mod")
        print_logger.info("Welcome to CoffeeForYou!")
        user = EntryMenu()
        progress_logger.info("Entry_menu passed")
        action = ActionMenu(user)
        progress_logger.info("Action_menu passed")
    else:
        progress_logger.info("Programm started in cmdline mod with args : {}".format(cmd_args))
        user = EntryMenu(username=cmd_args.name, position=cmd_args.pos, operation=cmd_args.reg)
        progress_logger.info("Entry menu passed")
        action = ActionMenu(user, action=cmd_args.action,
                            beverage=cmd_args.bev, add=cmd_args.add)
        progress_logger.info("Action menu passed")
    progress_logger.info("Session finished")


if __name__ == '__main__':
    entry()
