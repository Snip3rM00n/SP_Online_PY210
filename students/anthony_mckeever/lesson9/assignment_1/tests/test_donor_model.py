"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""

from ..donor_models import Donor
#from donor_models import Donor

def test_donor_init():
    donor = Donor("Sophia McLoaphia", [99.00])
    assert donor.name == "Sophia McLoaphia"
    assert donor.donations[0] == 99.0
    assert len(donor.donations) == 1


def test_append():
    donor = Donor("Sophia McLoaphia", [99.00])
    donor.accept_donation(200.23)
    assert donor.donations[-1] == 200.23


def test_total():
    donor = Donor("Sophia McLoaphia", [99.00])
    donor.accept_donation(1.00)
    assert donor.total_donations == 100.0


def test_avg():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    assert donor.average_donation == 75.0


def test_summary():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    s = ("Sophia McLoaphia", "150.00", 2, "75.00")
    assert donor.to_summary == s


def test_get_email():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    test_email = f"{donor.name} - {donor.donations[-1]}"
    assert donor.get_email("{} - {}") == test_email


def test_len():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    assert len(donor) == 2


def test_str():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    assert str(donor) == "Sophia McLoaphia,50.00,100.00"


def test_lt():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    donor2 = Donor("Sophia McLoaphia", [100.00, 100.00])
    assert donor < donor2
    assert donor2 > donor


def test_eq():
    donor = Donor("Sophia McLoaphia", [50.00, 100.00])
    donor2 = Donor("Sophia McLoaphia", [50.00, 100.00])
    assert donor == donor2


def test_from_string():
    donor = Donor.from_string("Sophia McLoaphia,50.00,100.00")
    assert donor.name == "Sophia McLoaphia"
    assert donor.donations == [50.0, 100.0]