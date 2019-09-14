"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

import io
import sys
import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from .. import cli_main
from .shared_methods import TestHelpers


class mock_args():
    donor_list = "./donor_list.csv"
    email_template = "./email_template.csv"


class TestMain(TestCase):

    def test_main_golden_path(self):
        with patch('builtins.input') as handle_input:
            handle_input.return_value = "4"
            open_mock = mock.mock_open()
            cli_main.donor_list = TestHelpers.get_donor_collection()
            
            with patch("os.path.isdir") as is_dir:
                is_dir.return_value = True

                with patch("builtins.open", open_mock, create=True):
                    with self.assertRaises(SystemExit):
                        cli_main.main(mock_args)
                        