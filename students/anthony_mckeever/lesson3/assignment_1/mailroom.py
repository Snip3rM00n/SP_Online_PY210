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
        * As a user I want to get a report of donors, their total donated and how many times they've donated.
    User Interactivity:
        As a user I want to return to the main menu
        As a user I want to quit the script.
"""

menu_opts = ["main", "return", "stop"]
quit_opts = ["exit", "end", "quit"]
list_opts = ["list", "l", "ls"]
help_opts = ["help", "h", "?"]
stay_on = True

def main():
    print("\nStudio Starchelle Donor Appreciation System\n")
    while stay_on:
        print_menu()
        user_choice = input("What do you want to do? > ")
        handle_main_choice(user_choice.lower())

def print_menu():
    help_cmds = ", ".join(help_opts)
    print("--- Main Menu ---\n"
          "\nAvailable Options:\n"
          "\t\"Send A Thank You\"\tGet prepopulated email template to thank a donor.\n"
          "\t\"Create a Report\"\tView a list of all donors and their cumulative donations.\n"
          f"\t\"{help_cmds}\t\tView the script's help text and additional commands.\n"
         )

def handle_main_choice(user_choice):
    if user_choice in help_opts:
        print_help()
    elif user_choice == "create a report":
        create_report()
    elif user_choice == "send a thank you":
        send_thanks()
    elif user_choice in quit_opts:
        global stay_on
        stay_on = False
    else:
        print("\nUnknown command.\n"
              "Type \"help\" to get all options.\n")

def print_help():
    help_cmds = ", ".join(help_opts)
    quit_cmds = ", ".join(quit_opts)
    menu_cmds = ", ".join(menu_opts)
    print("\nStudio Starchelle Donor Appreciation System\n"
          "\nA basic system for thanking donors for thier generous contributions.\n"
          "\nCommand List:\n"
          f"\t{help_cmds}\t\tPrints this help text.\n"
          f"\t{menu_cmds}\tReturn to the main menu.\n"
          f"\t{quit_cmds}\t\tExit the entire script.\n"
         )
    input("\n--- Press the Enter/Return Key to return to Main ---\n")
    

def send_thanks():
    pass

def create_report():
    donor_summary = []
    skip = []
    for donor in donors_list:
        if donor[0] not in skip:
            skip.append(donor[0])
            donor_entries = [x for x in donors_list if x[0] == donor[0]]
            donor_summary.append(process_donor(donor_entries))

    print_table(donor_summary)

def print_table(donor_summary):
    header = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    lengths = get_lengths(donor_summary, header)
    table = []

    sep_strings = [("-" * (lengths[0] + 2)), ("-" * (lengths[1] + 2)), ("-" * (lengths[2] + 2)), ("-" * (lengths[3] + 2))]
    sep_line = "|" + "+".join(sep_strings) + "|"
    donor_summary2 = sorted(donor_summary, key=lambda x: x[1])

    for item in donor_summary2:
        table.append(format_line(item, lengths))
        table.append(sep_line)

    report_name = "Donor Report"
    table.insert(0, "\n|" + "-" * (len(sep_line) - 2) + "|")
    table.insert(1, f"|{report_name:^{len(sep_line) -2}}|")
    table.insert(2, sep_line)
    table.insert(3, format_line(header, lengths, is_donor=False))
    table.insert(4, sep_line)

    print("\n".join(table) + "\n")

def format_line(item, lengths, is_donor=True):
    if is_donor:
        total = f"${item[1]:.02f}"
        avg = f"${item[3]:.02f}"
        return f"| {item[0]:<{lengths[0]}} | {total:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {avg:>{lengths[3]}} |"
    return f"| {item[0]:<{lengths[0]}} | {item[1]:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {item[3]:>{lengths[3]}} |"

def process_donor(donor_entries):
    name = ""
    total_donations = 0.0
    count_donations = 0
    
    for donor in donor_entries:
        if name == "":
            name = donor[0]
        count_donations += 1
        total_donations += donor[1]
    
    average_donation = total_donations / count_donations

    return (name, total_donations, count_donations, average_donation)
        
def get_lengths(seq, header):
    name_len = len(header[0])
    total_len = len(header[1])
    count_len = len(header[2])
    avg_len = len(header[3])
    
    for item in seq:
        total = f"${item[1]:.02f}"
        count = str(item[2])
        avg = f"${item[3]:.02f}"

        name_len = len(item[0]) if len(item[0]) > name_len else name_len
        total_len = len(total) if len(total) > total_len else total_len
        count_len = len(count) if len(count) > count_len else count_len
        avg_len = len(avg) if len(avg) > avg_len else avg_len

    return [name_len, total_len, count_len, avg_len]
