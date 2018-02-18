#!/usr/bin/python
# ! -*- coding: utf-8 -*-

__author__ = "Popov Dmitriy"

from body.constants import *
import argparse



def get_args():
    parser = argparse.ArgumentParser(description=HelpsAndChoices.DESCRIPTION)
    parser.add_argument('-cmd', action='store_const', const=True, default=False,
                        help=HelpsAndChoices.CMD_HELP)
    parser.add_argument('-u', '--username', dest='name', type=str, default=None, nargs="+",
                        help=HelpsAndChoices.USERNAME_HELP)
    parser.add_argument('-p', '--position', dest="pos", choices=['Salesman', 'Manager'], default=None, type=str,
                        help=HelpsAndChoices.POSITION_HELP)
    parser.add_argument('-reg','--registration', dest="reg", action='store_const', const="2", default="1",
                        help=HelpsAndChoices.ADD_USER_HELP)
    parser.add_argument('-action', choices=["1", "2", "3", "4", "5"], default=None, type=str,
                        help=HelpsAndChoices.ACTION_HELP)
    parser.add_argument('-b', '--beverage', dest='bev', type=str, default=None, choices=HelpsAndChoices.BEVERAGE_CHOICES,
                        help=HelpsAndChoices.BEVERAGE_HELP)
    parser.add_argument('-a', "--additionals", dest="add", type=str, default=None, choices=HelpsAndChoices.ADDS_CHOICES,
                        help=HelpsAndChoices.ADDS_HELP)
    namespace = parser.parse_args()
    if not namespace.name is None:
        namespace.name = " ".join(namespace.name)
    return namespace

def get_right_name(name_list):
    return " ".join(name_list)