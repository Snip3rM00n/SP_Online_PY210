"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import os.path

from support import Helpers

class Donor():

    def __init__(self, name, donations):
        self.donor_name = name
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
    def from_string(cls, input):
        input = input.split(',')
        name = input[0]
        donations = [float(d) for d in input[1:]]
        self = cls(name, donations)
        return self

    
    @property
    def to_summary(self):
        return (self.donor_name, f"{self.total_donations:.02f}", len(self), f"{self.average_donation:.02f}")


    def __len__(self):
        return len(self.donations)

    def __str__(self):
        donations = ",".join([f"{d:.02f}" for d in self.donations])
        return f"{self.donor_name},{donations}"


    def __lt__(self, other):
        tuple_self = (self.total_donations, self.average_donation) 
        tuple_other = (other.total_donations, other.average_donation)
        return tuple_self < tuple_other


class Donor_Collection():

    def __init__(self, list_donors):
        self.donors = list_donors


    @classmethod
    def from_file(cls, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No file exists at path: {file_path}")

        donors = []
        with open(file_path, "r") as in_file:
            content = in_file.readline()
            while len(content) > 0:
                print(content)
                donors.append(Donor.from_string(content))
                content = in_file.readline()
        
        self = cls(donors)
        return self

    
    @property
    def donor_summary(self):
        #header = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
        #lengths = Helpers.get_legnths(summaries, header)
        return [d.to_summary() for d in self.donors]


    def write_donors(self, file_path):
        with open(file_path, "w") as out_file:
            content = "\n".join([str(d) for d in self.donors])
            out_file.writelines(content)


    def save_to_file(self, file_path):
        dir_name = os.path.dirname(file_path)
        if not os.path.isdir(dir_name):
            raise NotADirectoryError(f"No directory exists at: {dir_name}")

        try:
            self.write_donors(file_path)
            print(f"Donor list backed up to: {file_path} successfully.")
        except Exception as e:
            new_file_path = os.path.join(os.path.curdir(), "donor_list.csv")
            self.write_donors(file_path)

            msg = str(f"Could not write file to: {file_path}\n"
                      f"The donor list has been backed up to: {new_file_path}")
            raise IOError(msg) from e
