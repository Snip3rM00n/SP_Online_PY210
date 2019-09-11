"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 
"""


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
        Return the max length between the longest item in a sequence or the name of the field.

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


class MenuDriven():

    def __init__(self):
        pass