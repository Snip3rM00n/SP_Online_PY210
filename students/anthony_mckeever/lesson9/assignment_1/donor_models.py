"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import os.path

from support import Helpers
from support import File_Helpers

class Donor():

    def __init__(self, name, donations):
        self.name = name
        self.donations = [d for d in donations]

    
    def accept_donation(self, amount):
        self.donations.append(amount)


    @property
    def total_donations(self):
        return sum(self.donations)


    @property
    def average_donation(self):
        return self.total_donations / len(self)


    @classmethod
    def from_string(cls, in_value):
        in_value = in_value.split(',')
        name = in_value[0]
        donations = [float(d) for d in in_value[1:]]
        self = cls(name, donations)
        return self

    
    @property
    def to_summary(self):
        return (self.name, f"{self.total_donations:.02f}",
                len(self), f"{self.average_donation:.02f}")


    def get_email(self, template):
        donation = f"{self.donations[-1]:.02f}"
        return template.format(self.name, donation)


    def __len__(self):
        return len(self.donations)


    def __str__(self):
        donations = ",".join([f"{d:.02f}" for d in self.donations])
        return f"{self.name},{donations}"


    def __lt__(self, other):
        tuple_self = (self.total_donations, self.average_donation) 
        tuple_other = (other.total_donations, other.average_donation)
        return tuple_self < tuple_other

    
    def __eq__(self, other):
        return self.to_summary == other.to_summary


class Donor_Collection():

    def __init__(self, list_donors, email_template):
        self.donors = list_donors
        self.email_template = File_Helpers.open_file(email_template, type(str()))


    @classmethod
    def from_file(cls, file_path, email_template):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No file exists at path: {file_path}")

        donors = [Donor.from_string(c) for c in File_Helpers.open_file(file_path, type(Donor))]

        self = cls(donors, email_template)
        return self


    def handle_donation(self, name):
        donation = 0.0
        while donation <= 0.0:
            amount = Helpers.safe_input("How much did they donate?")
            
            if amount.lower() == "cancel":
                return
            
            donation = Helpers.validate_donation(amount)

        donor = self[name]

        if donor is not None:
            donor.accept_donation(donation)
        else:
            donor = Donor(name, [donation])
            self.donors.append(donor)

        Helpers.print_email(donor.get_email(self.email_template))
    
    @property
    def donor_summary(self):
        return [d.to_summary for d in self.donors]


    @property
    def get_names(self):
        donors = "\n\t".join([d.name for d in self.donors])
        return f"\t{donors}"


    def write_donors(self, file_path, msg=None):
        content = "\n".join([str(d) for d in self.donors])
        File_Helpers.write_file(file_path, content, msg)


    def save_to_file(self, file_path):
        dir_name = os.path.dirname(file_path)
        if not os.path.isdir(dir_name):
            raise NotADirectoryError(f"No directory exists at: {dir_name}")

        try:
            msg = f"Donor list backed up to: {file_path} successfully."
            self.write_donors(file_path, msg)
        except Exception as e:
            new_file_path = os.path.join(os.path.curdir, "donor_list.csv")

            msg = str(f"Could not write file to: {file_path}\n"
                      f"The donor list has been backed up to: {new_file_path}")

            self.write_donors(file_path, msg)
            raise IOError(msg) from e
    

    def __getitem__(self, index):
        if isinstance(index, str):
            return next((d for d in self.donors if d.name == index), None)
        else:
            return  self.donors[index]


    def __len__(self):
        return len(self.donors)
