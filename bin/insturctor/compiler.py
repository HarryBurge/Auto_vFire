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
import copy
from bin.insturctor.compilerUtil import ruleset
from bin.insturctor.compilerUtil import ruleset_internal_structure as button


def current_CWD(rules, current_stack):
    '''
    Takes the stack which is basicaaly a path from the opening
    of vFire to that button.

    params:-
        rules : Ruleset : rules to follow by with the buttons
    returns:-
        [_button, [str, ...], ...] : Buttons in CWD with path to them
    '''

    # Initilises path and CWD to starting values
    path = [rules.buttonRules.getName()]
    CWD = [[k, copy.copy(path)] for k in rules.buttonRules.globals]

    # Used to keep track of the button we are on when going down the rules
    current_button = rules.buttonRules

    # Cycles through the pathing of the stack
    for i in current_stack:

        # Searchs through all child buttons of current_button
        for j in current_button.locals + current_button.globals:
            
            if j.getName() == i:

                # Pretend button was pressed so path changes
                path.append(j.getName())

                # Current button changes to the one pressed
                current_button = j

                # Add all globals to CWD cause they don't delete like locals do
                for k in j.globals: CWD.append([k, copy.copy(path)])
    
    # Now all globals are found give the locals of the last button
    for k in current_button.locals: CWD.append([k, copy.copy(path)])

    return CWD


def check_in_CWD(CWD, button_press):
    '''
    Check if a button is within the CWD
    
    params:-
        CWD : [_button, [str, ...], ...] : Buttons in CWD with path to them
        button_press : str : Button that wants to be pressed
    returns:-
        bool : True if in CWD, False otherwise
    '''

    for i in CWD:
        if i[0].getName() == button_press: return True
    return False


def compile(instructions, name='compiled', ruleset_path=os.path.dirname(os.path.realpath(__file__))+'/config/commands_and_rules.txt'):
    '''
    Compiles a bunch of instructions passed and outputs them to a file which
    can then be used to implement the changes in vfire using vFire controller

    params:-
        instructions : [str, ...] : Lines passed from the file wanting to be compiled
        name : str : Filename of the output file
        ruleset_path : str : Path to file for the ruleset being used
    returns:-
        None
    '''

    # Compiled file which will run the commands given in the instructions
    output_file = open(name + '.txt', 'w')

    # Used to keep track of where we are within vFire and what buttons are veiwable
    stack = ['vFire']
    
    # Creates a ruleset from the file passed
    rules = ruleset.RuleSet(ruleset_path)

    # Loop through instructions to get path from vFire
    instructions_path = []

    for i in instructions:

        # Get current working directory depending on prevouis stack
        CWD = current_CWD(rules, stack)

        # Check if instruction is in ruleset
        if check_in_CWD(CWD, i):

            # Find the button and get the path for it
            for j in CWD:
                if j[0].getName() == i:
                    temp_stack = j[1]

            # Check the buttons path compared to current dir
            if stack != temp_stack:
                stack = temp_stack + [i]
            else:
                stack.append(i)

            # Output the full path to the button
            instructions_path.append(copy.copy(stack))
        
        elif i in rules.customCommands:

            for j in rules.customCommands[i]:

                # Get current working directory depending on prevouis stack
                CWD = current_CWD(rules, stack)

                # Check if instruction is in ruleset
                if check_in_CWD(CWD, j):

                    # Find the button and get the path for it
                    for k in CWD:
                        if k[0].getName() == j:
                            temp_stack = k[1]

                    # Check the buttons path compared to current dir
                    if stack != temp_stack:
                        stack = temp_stack + [j]
                    else:
                        stack.append(j)

                    # Output the full path to the button
                    instructions_path.append(copy.copy(stack))

                else:
                    raise RuntimeError('Custom command cannot be exectuted either due to being errored or in the wrong section before the command')

        else:
            raise RuntimeError('Syntax error, not a command in ruleset at line ' + str(instructions.index(i)+1))

    # Format the array into a output file
    for i in instructions_path:

        temp = ''

        for j in i:

            temp += str(j) + '-'

        temp = temp[:-1]

        output_file.write(temp + '\n')




    
    
    