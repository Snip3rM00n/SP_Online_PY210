"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""
import os
import sys
import tempfile


class Helpers():
    
    @staticmethod
    def get_legnths(summaries, headers):
        return [Helpers.get_length([x[0] for x in summaries], headers[0]),
                Helpers.get_length([x[1] for x in summaries], headers[1]),
                Helpers.get_length([x[2] for x in summaries], headers[2]),
                Helpers.get_length([x[3] for x in summaries], headers[3])]


    @staticmethod
    def get_length(seq, name):
        """
        Return the max length between the longest item in a sequence or the
        name of the field.

        :seq:   The sequence to evaluate
        :name:  The name of the field to evaluate
        """
        longest = sorted(seq, key=Helpers.length_key, reverse=True)[0]
        return max(len(name), len(str(longest)))


    @staticmethod
    def length_key(item):
        """
        The sort key for the length of items in a sequence
        """
        return len(str(item))


    @staticmethod
    def get_table(header, lengths, summaries, report_name="Donor Summary Report"):
        sep_strings = ["-" * (x + 2) for x in lengths]
        sep_line = "|" + "+".join(sep_strings) + "|"
        table = ["\n|" + "-" * (len(sep_line) - 2) + "|",
                  f"|{report_name:^{len(sep_line) - 2}}|",
                  sep_line,
                  Helpers.format_line(header, lengths),
                  sep_line]

        table.extend([Helpers.format_line(d, lengths) + f"\n{sep_line}" for d in summaries])
        return table


    @staticmethod
    def format_line(item, lengths):
        """
        Return a formatted string that will fit in the donor summary table.
    
        :item:      The sequence of data to format.
        :lengths:   The lengths for each field of the table.
        """
        return str(f"| {item[0]:<{lengths[0]}} | {item[1]:>{lengths[1]}} | "
                   f"{item[2]:>{lengths[2]}} | {item[3]:>{lengths[3]}} |")


    @staticmethod
    def safe_input(prompt):
        output = None
        try:
            output = input(f"\n{prompt} > ")
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
            sys.exit()
        else:
            return output


    @staticmethod
    def validate_donation(amount):
        try:
            donation = float(amount)
        except ValueError:
            donation = 0.0
        finally:
            if donation <= 0.0:
                print("Invalid amount.  Try again.")
            return donation

        
    @staticmethod
    def print_email(email):
        print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")
        print(email)
        print("\n\n----- PLEASE SEND THIS EMAIL TO THE DONOR -----\n\n")


class File_Helpers():

    @staticmethod
    def open_file(file_path, output_type):
        with open(file_path, "r") as in_file:
            if output_type is type(str()):
                return in_file.read()
            else:
                return in_file.readlines()


    @staticmethod
    def write_file(file_path, content, finish_msg=None):
        with open(file_path, "w") as out_file:
            if isinstance(content, list):
                out_file.writelines(content)
            else:
                out_file.write(content)
        
        if finish_msg is not None:
            print(finish_msg)


    @staticmethod
    def get_user_output_path():
        """
        Return the user's desired path for emails or None if the user leaves the choice blank.
        Will prompt to create a directory if it does not exist.
        """
        default_dir = tempfile.gettempdir()

        print(f"\nDefault Directory: {default_dir}")

        user_dir = Helpers.safe_input("Please enter a directory (Empty for Default, \"Cancel\" to return to main menu)")
        user_dir = user_dir.lower()

        if user_dir != "" and user_dir != "cancel":
            if not os.path.exists(user_dir):
                while True:
                    choice = Helpers.safe_input(f"The directory \"{user_dir}\" does not exist.  Do you want to create it? ([Y]es / [N]o)")
                    if choice.lower() in ["yes", "y"]:
                        os.makedirs(user_dir)
                        break
                    elif choice.lower() in ["no", "n"]:
                        print("Using default directory instead.")
                        user_dir = default_dir
                        break
                    print("Invalid choice.  Please enter \"Yes\" or \"No\"")
        elif user_dir != "cancel":
            return default_dir
        elif user_dir == "cancel":
            return None

        return user_dir


class MenuItem():

    def __init__(self, name, description, method, tabs=2, kwargy=False):
        self.name = name
        self.description = description
        self.method = method
        self.total_tabs = tabs
        self.kwargy = kwargy

    
    def __str__(self):
        tabs = "\t" * self.total_tabs
        return self.name if self.description is None else f"{self.name}{tabs}{self.description}"


class MenuDriven():

    def __init__(self, menu_text, menu_items, prompt_string, show_main=False, invalid=None):
        self.menu_text = menu_text
        self.prompt = prompt_string
        self.menu_items = {str(i+1): m for i, m in enumerate(menu_items)}
        self.invalid_option = invalid

        if show_main:
            main_entry = MenuItem("Return to Main Menu", None, None)
            self.menu_items.update({str(len(self.menu_items)+1): main_entry})

        exit_entry = MenuItem("Exit the Script", None, sys.exit)
        self.menu_items.update({str(len(self.menu_items)+1): exit_entry})
    

    def print_menu(self):
        print(f"\n{self.menu_text}")
        for k, v in self.menu_items.items():
            print( f"\t{k} - {str(v)}")


    def run_menu(self):
        self.print_menu()

        while True:
            user_choice = Helpers.safe_input(self.prompt)
            choice = self.menu_items.get(user_choice)

            if choice is not None:
                if choice.method:
                    choice.method()
                
                if choice.name != "List Donors":
                    break

            else:
                if self.invalid_option is None:
                    print("Invalid choice.  Please select from the available options.")
                else:
                    self.invalid_option(user_choice)
                    break