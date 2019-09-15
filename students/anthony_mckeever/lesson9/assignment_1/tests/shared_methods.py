"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import io
import sys

from unittest import mock
from unittest.mock import patch

from ..donor_models import Donor
from ..donor_models import Donor_Collection

class TestHelpers():

    donor_list = ["Sophia McLoaphia,50.00,100.00",
                  "Cresenta Starchelle,50.00,100.00",
                  "Anthony Crowley,10.20,30.40",
                  "Aziraphale,50000.00,10000.00",
                  "Anathema Device,60.00,70.00"]


    @staticmethod
    def get_donor_collection():
        open_mock = mock.mock_open(read_data="{} -- {}")
        with patch("builtins.open", open_mock, create=True):
            donors = [Donor.from_string(d) for d in TestHelpers.donor_list]
            collection = Donor_Collection(donors, "idk_some_file_okay.txt")
        
        return collection


    @staticmethod
    def intercept_stdout():
        hold_stdout = sys.stdout
        interceptor = io.StringIO()
        sys.stdout = interceptor

        return interceptor, hold_stdout


    @staticmethod
    def multi_open_mock(file_name, __):
        if file_name == "probably_not_a_file.txt":
            content = "\n".join(TestHelpers.donor_list)
        elif file_name == "totes_a_real_file.txt":
            content = "{} -- {}"
        else:
            raise FileNotFoundError(f"Fuck {file_name}")
        
        file_object = mock.mock_open(read_data=content).return_value
        file_object.__iter__.return_value = TestHelpers.donor_list
        return file_object

    
    @staticmethod
    def mock_open_errors(file_name, __):
        if file_name.count("pls_fail") > 0:
            content = Exception("Test Failure")
        else:
            content = ""
        
        file_object = mock.mock_open(read_data=content).return_value
        return file_object
