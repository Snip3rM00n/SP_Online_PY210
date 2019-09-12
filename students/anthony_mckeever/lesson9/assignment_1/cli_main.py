"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import argparse
import sys

from support import MenuItem
from support import MenuDriven
from donor_models import Donor
from donor_models import Donor_Collection


parser = argparse.ArgumentParser(description="Studio Starchelle's Donor Appreciation System")
parser.add_argument("--donor-list", type=str, default="./donor_list.csv")


def send_thanks():
    pass


def create_report():
    pass


def send_to_all():
    pass


main_menu = [
    MenuItem("Send a Thank You", "Get email template to thank a donor.", send_thanks),
    MenuItem("Create a Report", "View a list of all donors and their cumulative donations", create_report),
    MenuItem("Send Letters to All", "Generate a letter for every donor.", send_to_all)
]
main_menu = MenuDriven("Main Menu:", main_menu, "What do you want to do? > ")

if __name__ == "__main__":
    args = parser.parse_args()
    donor_list = Donor_Collection.from_file(args.donor_list)

    try:
        main_menu.run_menu()
    except SystemExit:
        donor_list.save_to_file(args.donor_list)
        raise
