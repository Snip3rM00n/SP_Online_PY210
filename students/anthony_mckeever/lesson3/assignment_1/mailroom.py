"""
Programming In Python - Lesson 3 Assignment 1: Mailroom Part 1
Code Poet: Anthony McKeever
Start Date: 07/31/2019
End Date: 
"""

donors_list = [("Cresenta Starchelle", 99.99),
               ("Cresenta Starchelle", 29.99),
               ("Delilah Matsuka", 199.99),
               ("Delilah Matsuka", 299.99),
               ("Astra Matsume", 599.99),
               ("Astra Matsume", 799.99)]

"""
User Stories:
    Send Thank You:
        As a user I want to get a list of my donors to see who's donated.
        As a user I want to be able to thank a new donor
        As a user I want to know how much they've donated in total.
        As a user I want to add to the donor's donation history.
        As a user I want to get a populated email template to send to the donor thanking them.
    Create Report:
        As a user I want to get a report of donors, their total donated and how many times they've donated.
        As a user I want to return to the main menu
        As a user I want to quit the script.
"""

def create_report():
    donor_summary = []
    for donor in donors_list:
        name = donor[0]
        total = donor[1]

        if donor_summary.count(name) < 1:
