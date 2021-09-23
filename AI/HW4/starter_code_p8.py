import sys
from itertools import product


# Class to create Nodes
class Node(object):

    # Constructor
    def __init__(self, name):
        self.parents = []
        self.children = []
        self.name = name
        self.is_prior = True
        self.prob_table = {}

    # Function to Add Child
    # I/p Argument - child (str): child to add
    def add_child(self, child):
        self.children.append(child)

    # Function to Add Parents
    # I/p Argument - parents (list of str): list of parent to add
    def add_parents(self, parents):
        self.parents.extend(parents)

    # Add any additional functions you need


# Class to Construct the bayesian network as a graph
class BayesianNetwork(object):
    pass

    # Write functions to construct the CPT Table and Construct the bayesian network as a graph
    # Your Code here


# Main - Calculate the probablities asked in the question
def main():
    burglary = 'Burglary'
    alarm = 'Alarm'
    earthquake = 'Earthquake'
    john_calls = 'JohnCalls'
    mary_calls = 'MaryCalls'
    edges = [
        [burglary, alarm],
        [earthquake, alarm],
        [alarm, john_calls],
        [alarm, mary_calls]
    ]
    pAlarmColums = [burglary, earthquake, alarm]
    pAlarm = [
        ('t', 't', 0.95),
        ('t', 'f', 0.94),
        ('f', 't', 0.29),
        ('f', 'f', 0.001),
    ]
    pJohncalls = [br]
    pass
    # Your Code here


if __name__ == "__main__":
    main()
