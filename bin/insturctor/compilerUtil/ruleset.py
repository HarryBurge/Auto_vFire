'''
This is the ruleset class.
'''

__Authour__ = 'Harry Burge'
__DateCreated__ = '07/02/2020'
__LastUpdated__ = '07/02/2020'


# Imports
import copy
import bin.insturctor.compilerUtil.ruleset_internal_structure as Util


class RuleSet:
    '''
    A custom class which is used in the creation and testing of a ruleset.

    attributes:-
        buttonRules : 
        customCommands : {str : [str, ...]} : command name key, then commands
    '''

    def __init__(self, ruleset_path):
        '''
        Takes a path to a txt file that has the ruleset in it

        params:-
            ruleset_path : str : the path to the text file
        returns:-
            None
        '''

        # Read file passed
        file = open(ruleset_path, 'r')
        lines = file.read().split('\n')
        file.close()

        # Remove annotations and clear lines
        temp = []
        for line in lines:
            if line != '' and line.find('#') == -1: temp.append(line)

        # Initilise the ruleset
        self.buttonRules = self._get_button_rules(copy.copy(temp))
        self.customCommands = self._get_custom_commands(copy.copy(temp))


    def __str__(self):
        '''
        Creates a string of all the things.

        params:-
            None
        returns:-
            str : the string of things
        '''
        tempbuttons = ''
        for i in self.buttonRules:
            tempbuttons += '\n' + str(i)

        return 'Custom Commands:-\n' + str(self.customCommands) + '\n\nButton Rules:-' + tempbuttons


    def _get_button_rules(self, lines):
        '''
        Takes the lines passed from the file and puts them into a datastructure which
        holds the infomation which will be used, to test the actual compilation.

        params:-
            lines : [str, ...] : lines passed from the file
        returns:-
            [button, ...] : makes the rules of buttons
        '''

        rules = []

        # Check for the @ButtonRules section and remove all lines before
        try:
            del lines[:lines.index('@ButtonRules')+1]
        except ValueError:
            raise RuntimeError('@ButtonRules section neeeded')

        # Check if the @CustomCommands section is below and delete lines if approiate
        try:
            del lines[lines.index('@CustomCommands'):]
        except ValueError:
            None

        # Lines in the form [(*)thing, ..., (*)thing2, \t(*)thing, ...]
        # Global = *, Local = -

        # Put lines into form specifyed
        rules = Util.recursive_read(lines)

        return rules

    
    def _get_custom_commands(self, lines):
        '''
        Takes lines passed, finds if it has customcommands section, then creates
        a dictonary of the commands.

        params:-
            lines : str : lines read in from the ruleset file
        returns:-
            {str : [str, ...]} : Customcommand as key then array of commands which make it
        '''

        rules = {}

        # Check for the @CustomCommands section and remove all lines before
        try:
            start_index = lines.index('@CustomCommands')
            del lines[:start_index+1]
        except ValueError:
            return rules

        # Check if the @ButtonRules section is below and delete lines if approiate
        try:
            del lines[lines.index('@ButtonRules'):]
        except ValueError:
            None

        # Lines in form [thing, \tthing, ..., thing2, \tthing2, ...]

        # Put lines into form specifyed
        stack = None

        for line in lines:

            if line.find('\t') == -1:
                rules[line] = []
                stack = line

            else:
                rules[stack].append(line.replace('\t',''))

        return rules