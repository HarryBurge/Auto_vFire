'''
This is what can compile a text file that was passed by Auto_vFire.
It checks validity of commands passed and then will create a new
file that can then be executed.
'''

__Authour__ = 'Harry Burge'
__DateCreated__ = '01/02/2020'
__LastUpdated__ = '04/02/2020'


# Imports
import os
from bin.insturctor.compilerUtil import ruleset


def compile(instructions,ruleset_path=os.path.dirname(os.path.realpath(__file__))+'/config/commands_and_rules.txt'):
    
    # Creates a ruleset from the file passed
    rules = ruleset.RuleSet(ruleset_path)
    
    # Loop over all commands and check for validity

