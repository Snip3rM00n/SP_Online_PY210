"""
Programming In Python - Lesson 4 Assignment 1: Mailroom Part 2
Code Poet: Anthony McKeever
Start Date: 08/06/2019
End Date: 
"""
import sys

def main():
    """
    The main loop of the script.  Prompts user with a main menu.
    """
    print("\nStudio Starchelle Donor Appreciation System\n")
    while True:
        menu_system(main_menu_dict, "\nMain Menu:", "\nWhat do you want to do? > ")
        #print_options()
        #user_choice = input("What do you want to do? > ")
        #handle_main_choice(user_choice.lower())

def menu_system(opts_dict, menu_text, prompt_text, include_main=False, include_donors=False, invalid_opt=None):
    show_opts = opts_dict.copy()
    
    if include_main:
        show_opts.update(main_dict)

    show_opts.update(quit_dict)

    print(menu_text)
    print_options(show_opts)
    
    # Don't include the list of donors in the help text so the user has to request them.
    if include_donors:
        show_opts.update(donors_list)

    while True:
        user_choice = input(prompt_text)
        choice_key = key_from_lower(user_choice, show_opts.keys())

        if choice_key is not None:
            selection = show_opts[choice_key]
            if selection[1]:
                if selection[1] == accept_donation:
                    selection[1](choice_key)
                else:
                    selection[1]()
            
            break

        else:
            if invalid_opt is None:
                print("Invalid choice.  Please select from available options.")
            else:
                invalid_opt(user_choice)
                break

def key_from_lower(user_choice, keys):
    lower_keys = {k.lower() : k for k in keys}
    return lower_keys[user_choice] if user_choice in lower_keys.keys() else None

def get_opts_string(key, dictionary):
    count = sum(x == dictionary[key] for x in dictionary.values())
    if count < 1:
        return key, None
    else:
        opts = []
        for k, v in dictionary.items():
            if v == dictionary[key]:
                opts.append(k)
        return ", ".join(opts), opts

def print_donors():
    print("\nList of Donors:")
    for donor in donors_list.keys():
        print("\t" + donor)


def print_options(show_opts):
    skip = set([])
    for key, value in show_opts.items():
        if key not in skip:
            opts_string, skippable = get_opts_string(key, show_opts)
            print("\t" + opts_string + value[0])
            skip.update(skippable)


def send_thanks():
    """
    Function for acepting donations and thanking donors.
    print("\nLets send thanks!")
    thanking = True
    while thanking:
        user_choice = input("\nWho do you want to thank? > ")
        choice_key = key_from_lower(user_choice, donors_list.keys())
    """
    menu_system(list_dict, "\nLets send thanks!", "\nWho do you want to thank? > ", include_main=True, include_donors=True, invalid_opt=accept_donation)

def accept_donation(donor_name):
    donor = get_donor(donor_name)

    donation_float = 0.0
    while donation_float <= 0.0:
        donation = input("How much did they donate? > ")

        if donation in main_dict.keys():
            return
        elif donation in quit_dict.keys():
            quit_dict[donation][1]()

        donation_float = float(donation)
        if donation_float <= 0.0:
            print("Invalid amount.  Try again.")

    print(donation_float)
    donor[0].append(donation_float)
    print(donor[0])
    print(donors_list[donor_name])
    print_email(donor_name, donation_float)


def print_email(name, donation):
    """
    Print the thank you email to the console.

    :name:      The name of the donor.
    :donation:  The donation amount that was recieved from the donor.
    """
    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")
    print("Studio Starchelle - A Fizzworks Studios Company\n"
          "123 Starshine Ln.\n"
          "Suite 200\n"
          "New Sophiesville, WA, 99999\n"
          "StudioStarchelle@fakeemail.com\n\n"
         f"Dear {name},\n"
         f"\tThank you for your generous donation of ${donation:.02f} to our organization, Studio Starchelle.\n"
          "This kind offering will help us grow and expand the creative operations at Fizzworks\n"
          "Studios as well as finance the creation of new and exciting stories.\n\n"
          "\tYour donation gives you access to exclusive content from the Starchelle*Project universe.\n"
          "To view this content, please visit https://www.*********.com/donors and create an account using\n"
          "the code STARCHELLE1234.\n\n"
          "\tThank you once again for your kind donation.  With your help, we'll be able to make our next\n"
          "graphic novel, Starchelle*Project: Shooting Star, a reality!\n\n"
          "Sincerely,\n\n"
          "Sophia McKeever")
    print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")


def get_donor(user_choice):
    """
    Return the donor entry for the selected.  Creates a donor and appends them to donor_list if they do not exist.

    :user_choice:   The user's donor selection.
    """
    for donor in donors_list.keys():
        if user_choice.lower() == donor.lower():
            return donors_list[donor]
    
    donors_list.update({user_choice : ([], accept_donation)})
    return donors_list[user_choice]


def create_report():
    """
    Display a table of donors, the total amount they've donated, the count of their donations, and the average donation.
    """
    donor_summary = get_donor_summary()
    header = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    lengths = get_lengths(donor_summary, header)
    table = []

    sep_strings = [("-" * (lengths[0] + 2)), ("-" * (lengths[1] + 2)), ("-" * (lengths[2] + 2)), ("-" * (lengths[3] + 2))]
    sep_line = "|" + "+".join(sep_strings) + "|"
    for item in sorted(donor_summary, key=sort_key, reverse=True):
        table.append(format_line(item, lengths))
        table.append(sep_line)

    # Beautify report.
    report_name = "Donor Report"
    table.insert(0, "\n|" + "-" * (len(sep_line) - 2) + "|")
    table.insert(1, f"|{report_name:^{len(sep_line) -2}}|")
    table.insert(2, sep_line)
    table.insert(3, format_line(header, lengths, is_donor=False))
    table.insert(4, sep_line)

    print("\n".join(table) + "\n")


def sort_key(item):
    """
    The key to sort donors by.
    """
    return item[1]


def get_donor_summary():
    """
    Return a summary of all donors including their name, total donation sum, count of donations, and average donation.
    """
    donor_summary = []
    for donor in donors_list.keys():
        donor_amounts = donors_list[donor][0]
        name = donor

        total_donations = sum(donor_amounts)
        count_donations = len(donor_amounts)

        average_donation = total_donations / count_donations
        donor_summary.append([name, total_donations, count_donations, average_donation])
    return donor_summary


def format_line(item, lengths, is_donor=True):
    """
    Return a formatted string that will fit in the donor summary table.

    :item:      The sequence of data to format.
    :lengths:   The lengths for each field of the table.
    :is_donor:  A boolean value determining whether or not the :item: is a donor.  (Default = True)
    """
    if is_donor:
        total = f"${item[1]:.02f}"
        avg = f"${item[3]:.02f}"
        return f"| {item[0]:<{lengths[0]}} | {total:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {avg:>{lengths[3]}} |"
    return f"| {item[0]:<{lengths[0]}} | {item[1]:>{lengths[1]}} | {item[2]:>{lengths[2]}} | {item[3]:>{lengths[3]}} |"


def get_lengths(seq, header):
    """
    Return a list of the max lengths for all fields of the donor summary.
    
    :seq:       A list donor summary entries to get the lengths from.
    :header:    The header for the table to set the initial lengths to.
    """
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


main_menu_dict = { "Send A Thank You" : ("\tGet prepopulated email template to thank a donor.", send_thanks),
                   "Create a Report" :  ("\t\tView a list of all donors and their cumulative donations.", create_report) }

main_dict = { "main" :   ("\tReturn to the main menu.  Can be used at any input prompt.", None),
              "return" : ("\tReturn to the main menu.  Can be used at any input prompt.", None),
              "stop" :   ("\tReturn to the main menu.  Can be used at any input prompt.", None)
            }

quit_dict = { "exit" : ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
              "end" :  ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
              "quit" : ("\t\tQuit the script.  Can be used at any input prompt.", sys.exit),
            }

list_dict = { "list" : ("\t\tPrint a list of available donors.", print_donors),
              "l" :    ("\t\tPrint a list of available donors.", print_donors),
              "ls" :   ("\t\tPrint a list of available donors.", print_donors)
            }

donors_list = {"Cresenta Starchelle": ([99.99, 6000.00, 10345.23, 29.99], get_donor),
               "Delilah Matsuka"    : ([199.99, 299.99, 2100.00]        , get_donor),
               "Astra Matsume"      : ([599.99]                         , get_donor),
               "Kima Metoyo"        : ([3600.00, 1200.00]               , get_donor),
               "Kayomi Matsuka"     : ([0.01]                           , get_donor),
               "Katie Starchelle"   : ([600.00]                         , get_donor)}


if __name__ == "__main__":
    main()
