"""
Programming In Python - Lesson 3 Exercise 1: Slice Lab
Code Poet: Anthony McKeever
Start Date: 07/28/2019
End Date: 07/28/2019
"""

def format_sequence(seq):
    """
    Return a string that contains the contents of a sequence.  Each item will be formatted as following:
    seq[0] : Will be padded with up to 2 additional zeros.
    seq[1] : Will be formated to the second decimal place
    seq[2] : Will be formated in scientific notation to the second decimal.
    seq[3] : Will be formated in scientific notation to the second decimal.

    Example:
    Input: (2, 123.4567, 10000, 12345.67)
    Output: file_002 :  123.46, 1.00e+04, 1.23e+04

    :seq:   The sequence to format and recieve as string.
    """
    return "file_{:03d} :\t{:.2f}, {:.2e}, {:.2e}".format(*seq)

def format_sequence2(seq):
    """
    Return a string that contains the contents of a sequence.  Each item will be formatted as following:
    seq[0] : Will be padded with up to 2 additional zeros.
    seq[1] : Will be formated to the second decimal place
    seq[2] : Will be formated in scientific notation to the second decimal.
    seq[3] : Will be formated in scientific notation to the second decimal.

    Example:
    Input: (2, 123.4567, 10000, 12345.67)
    Output: file_002 :  123.46, 1.00e+04, 1.23e+04

    :seq:   The sequence to format and recieve as string.
    """
    return f"file_{seq[0]:03d} :\t{seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.2e}"

def format_numbers(seq):
    """
    Return a plural sensitve string that tells you how many numbers there are and what they are.

    Example:
    Input A: (0,)
    Output A: The 1 number is: 0

    Input B: (1, 2, 3)
    Output B: The 3 numbers are: 1, 2, 3

    :seq:   The sequence to format into the string.
    """
    size = len(seq)
    plural = "numbers are" if size > 1 else "number is"
    return ("The {} {}: " + ", ".join(["{:d}"] * size)).format(size, plural, *seq)

def format_five_integers(seq):
    """
    Return a string with the 5 integer sequence formated into "seq[3] seq[4] seq[0] seq[1] seq[2]"
    Each integer is padded by at least 1 zero.

    :seq:   The sequence to format into the string.
    """
    return f"{seq[3]:02d} {seq[4]:02d} {seq[2]:02d} {seq[0]:02d} {seq[1]:02d}"

def weigh_fruit(seq):
    """
    Return a string that displays the weight of each fruit.
    The sequence should contain two fruits and two weights in the pattern: ["fruit_a", fruit_a_weight, "fruit_b", fruit_b_weight]

    :seq:   The sequence to format into the string.
    """
    fruit_a = seq[0]
    an_a = get_grammar(fruit_a[:1])
    fruit_b = seq[2]
    an_b = get_grammar(fruit_b[:1])

    return f"The weight of {an_a} {fruit_a} is {seq[1]:.1f} and the weight of {an_b} {fruit_b} is {seq[3]:.1f}"

def weigh_fruit2(seq):
    """
    Return a string shows the percent difference of the weight of two fruits.
    The sequence should contain two fruits and two weights in the pattern: ["fruit_a", fruit_a_weight, "fruit_b", fruit_b_weight]

    :seq:   The sequence to format into the string.
    """
    fruit_a = seq[0]
    fruit_b = seq[2]
    an_a = get_grammar(fruit_a[:1])
    an_b = get_grammar(fruit_b[:1])

    weight_diff = round(seq[1] / seq[3], 1)
    weight_max, weight_min = max(1, weight_diff), min(1, weight_diff)

    size = "larger" if abs(weight_diff) > 1 else "smaller"
    display_weight = int((weight_max - weight_min) * 100)

    return f"The weight of {an_a} {fruit_a.upper()} is {display_weight}% {size} than the weight of {an_b} {fruit_b.upper()}."

def get_grammar(char):
    """
    Return a string of "an" if char is a vowel, or "a" if char is a consonant.

    :char:  The character to evaluate.
    """
    return "an" if char in ["a", "e", "i", "o", "u"] else "a"

def print_table(seq):
    """
    Return a string representing a table of Spacecrafts including a header.
    Header: ["Company:", "Name:", "Edition:", "Age:", "Cost:"]

    :seq:   The sequence to transform into a table.
    """
    table = []

    company_len = 8
    name_len = 5
    edition_len = 8
    age_len = 4
    cost_len = 5

    for item in seq:
        company = item[0]
        name = item[1]
        edition = item[2]
        age = item[3] 
        cost = item[4]

        company_len = len(company) if len(company) > company_len else company_len
        name_len = len(name) if len(name) > name_len else name_len
        edition_len = len(edition) if len(edition) > edition_len else edition_len
        age_len = len(str(age)) if len(str(age)) > age_len else age_len
        cost_len = len(str(cost)) if len(str(cost)) > cost_len else cost_len
        
        table.append(f"{company:<20} | {name:<20} | {edition:<20} | {age:<10}  | {cost:<10.02f} |")

    header = ["Company:", "Name:", "Edition:", "Age:", "Cost:"]
    table.insert(0, f"| {header[0]:<company_len} | {header[1]:<name_len} | {header[2]:<edition_len} | {header[3]:<age_len}  | {header[4]:<cost_len} |")
    return "\n".join(table)


def run_tests():
    print("Validate format_sequence")
    assert format_sequence((2, 123.4567, 10000, 12345.67)) == "file_002 :\t123.46, 1.00e+04, 1.23e+04"
    assert format_sequence((-1, 567.8910, 2, 555555.55555)) == "file_-01 :\t567.89, 2.00e+00, 5.56e+05"
    assert format_sequence((44444, 1.000235, 3452345234.2333212, 8)) == "file_44444 :\t1.00, 3.45e+09, 8.00e+00"

    print("Validate format_sequence2")
    assert format_sequence2((2, 123.4567, 10000, 12345.67)) == "file_002 :\t123.46, 1.00e+04, 1.23e+04"
    assert format_sequence2((-1, 567.8910, 2, 555555.55555)) == "file_-01 :\t567.89, 2.00e+00, 5.56e+05"
    assert format_sequence2((44444, 1.000235, 3452345234.2333212, 8)) == "file_44444 :\t1.00, 3.45e+09, 8.00e+00"

    print("Validate format_numbers")
    assert format_numbers((0,)) == "The 1 number is: 0"
    assert format_numbers((0, -1, 32)) == "The 3 numbers are: 0, -1, 32"
    assert format_numbers((333, 22 - 34, 2*2)) == "The 3 numbers are: 333, -12, 4"

    print("Validate format_five_integers")
    assert format_five_integers((4, 5, 3, 1, 2)) == "01 02 03 04 05"
    assert format_five_integers((-56, 50, 0, 11, 3458039485)) == "11 3458039485 00 -56 50"
    assert format_five_integers((20*5, 0, 0, 0, 3)) == "00 03 00 100 00"

    print("Validate weigh_fruit")
    assert weigh_fruit(["orange", 1.3, "lemon", 1.1]) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert weigh_fruit(["tomato", 1.1, "apple", 1]) == "The weight of a tomato is 1.1 and the weight of an apple is 1.0"
    assert weigh_fruit(["anti-banana", -1.4, "star fruit", 1.5]) == "The weight of an anti-banana is -1.4 and the weight of a star fruit is 1.5"

    print("Validate weigh_fruit2")
    assert weigh_fruit2(["coconut", 4, "lime", .5]) == "The weight of a COCONUT is 700% larger than the weight of a LIME."
    assert weigh_fruit2(["anti-lime", -.5, "lime", .5]) == "The weight of an ANTI-LIME is 200% smaller than the weight of a LIME."
    assert weigh_fruit2(["watermelon", 5, "anti-tomato", -1.1]) == "The weight of a WATERMELON is 550% larger than the weight of an ANTI-TOMATO."
    

if __name__ == "__main__":
    run_tests()

    seqx = [["Ekiya Glyde Company", "78 Glyde XL 2016", "Personal Edition", 3600, 20000000.00],
            ["Ekiya Glyde Company", "86 Glyde XL 3092", "Temporal Edition", 3600, 20000000.00],
            ["NASA", "Saturn V", "", 3600, 20000000.00],
            ["Ekiya Glyde Company", "92 Glyde Gx 2020", "Explorer Edition", 3600, 20000000.00]]