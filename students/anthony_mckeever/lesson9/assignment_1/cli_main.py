"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import argparse
import os.path

from support import Helpers
from support import File_Helpers

from support import MenuItem
from support import MenuDriven

from donor_models import Donor
from donor_models import Donor_Collection


parser = argparse.ArgumentParser(description="Studio Starchelle's Donor Appreciation System")
parser.add_argument("--donor-list", type=str, default="./resource/donor_list.csv")
parser.add_argument("--email-template", type=str, default="./resource/email_template.txt")


donor_list = None


def main(args):
    print("\nStudio Starchelle Donor Appreciation System")

    main_menu = [
        MenuItem("Send a Thank You", "Get email template to thank a donor.", send_thanks),
        MenuItem("Create a Report", "View all donors and their cumulative donations",
                 create_report),
        MenuItem("Send Letters to All", "Generate a letter for every donor.", send_to_all)
    ]
    main_menu = MenuDriven("Main Menu:", main_menu, "What do you want to do?")


    try:
        while True:
            main_menu.run_menu()
    except SystemExit:
        donor_list.save_to_file(args.donor_list)
        raise


def send_thanks():
    thanks = [MenuItem("List Donors", "Print a list of available donors.",
              print_donors, tabs=3)]
    thanks = MenuDriven("Lets Send Thanks!", thanks,
                        "Who would you like to thank? (Enter '1' to list donors)",
                        show_main=True, invalid=donor_list.handle_donation)
    thanks.run_menu()


def print_donors():
    print(donor_list.get_names)


def create_report():
    headers = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    summary = sorted(donor_list, reverse=True)
    summary = [d.to_summary for d in summary]
    lengths = Helpers.get_legnths(summary, headers)

    print("\n".join(Helpers.get_table(headers, lengths, summary)) + "\n")


def send_to_all():
    print("\n\nLets thank everybody!")
    print(str("\nThis will prepare a letter to send to everyone has donated to "
              "Studio Starchelle in the past."))
    print(str("All letters will be saved as text (.txt) files in the default directory a "
              "different directory is specified."))

    save_dir = File_Helpers.get_user_output_path()

    if save_dir is None:
        print("\nCancelling send to all.  Returning to main menu...\n")
        return
    
    for donor in donor_list:
        file_path = os.path.join(save_dir, f"{donor.name}.txt")
        File_Helpers.write_file(file_path, donor.get_email(donor_list.email_template))
    
    print(f"Donor letters successfully saved to: {save_dir}")


if __name__ == "__main__":
    args = parser.parse_args()
    donor_list = Donor_Collection.from_file(args.donor_list, args.email_template)

    main(args)
