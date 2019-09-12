"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""
import sys

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
    def safe_input(prompt):
        output = None
        try:
            output = input(prompt)
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
            sys.exit()
        else:
            return output


class MenuItem():

    def __init__(self, name, description, method):
        self.name = name
        self.description = description
        self.method = method

    
    def __str__(self):
        return self.name if self.description is None else f"{self.name}\t\t{self.description}"


class MenuDriven():

    def __init__(self, menu_text, menu_items, prompt_string, show_main=False, invalid=None):
        self.menu_text = menu_text
        self.prompt = prompt_string
        self.menu_items = {i+1: m for i, m in enumerate(menu_items)}
        self.invalid_option = invalid

        if show_main:
            main_entry = MenuItem("Return to Main Menu", None, None)
            self.menu_items.update({len(self.menu_items)+1: main_entry})

        exit_entry = MenuItem("Exit the Script", None, sys.exit)
        self.menu_items.update({len(self.menu_items)+1: exit_entry})
    

    def print_menu(self):
        print(self.menu_text)
        for k, v in self.menu_items.items():
            print( f"\t\n{k} - {str(v)}")


    def run_menu(self):
        self.print_menu()

        while True:
            user_choice = Helpers.safe_input(self.prompt)
            choice = self.menu_items.get(user_choice)

            if choice is not None:
                selection = self.menu_items[choice]

                if selection.method:
                    selection.method()
                
                if selection.name != "List Donors":
                    break

            else:
                if self.invalid_option is None:
                    print("Invalid choice.  Please select from the available options.")
                else:
                    self.invalid_option()
                    break