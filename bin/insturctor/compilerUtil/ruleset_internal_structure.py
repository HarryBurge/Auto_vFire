'''
This is some functions that are needed for the creation of a ruleset, also holds the class
for a button which is used in ruleset.
'''

__Authour__ = 'Harry Burge'
__DateCreated__ = '07/02/2020'
__LastUpdated__ = '07/02/2020'


def read_name_and_button(line):
    '''
    Used to clean up and make line usable in its seperate parts:

    params:-
        lines : str : in the form \t*<thing>, <num>
    returns:-
        (str, int) : in the form <name> <time>
    '''
    return line.split(',')[0].rstrip().lstrip().replace('\t',''), int(line.split(',')[1].rstrip().lstrip().replace('\t',''))


def index_of_next_same_level(lines, tablevel):
    '''
    Gets the first line in lines that has the same tab count. e.g. \t\tTom has 2 tablevel.

    params:-
        lines : [str, ...] : lines to search through
    returns:-
        int : the index of the next line with the same tablevel
    '''
    for index, line in enumerate(lines):

        if line.count('\t') == tablevel:
            return index


def recursive_read(lines):
    '''
    A recursive function which takes lines and will convert them into the buttons
    line[0] is the button being created and anything not on the tablevel
    belongs to button on line[0].

    params:-
        lines : [str, ...] : 0 index is the button being produced
    returns:-
        [button, ...] : returns a list of buttons with sub buttons underneath
    '''

    # Create button for line[0]
    button = _button(read_name_and_button(lines[0])[0], read_name_and_button(lines[0])[1])
    
    # If line[0] is the only one then return th empty button
    if len(lines) == 1:
        return [button]

    else:
        
        # Finds index fo the next line that has the same tablevel
        index = index_of_next_same_level(lines[1:], lines[0].count('\t'))

        # If next line is the same tablevel
        if index == 0:

            # Return empty button
            temp = [button]

            # Carry on the function
            for i in recursive_read(lines[index+1:]):
                temp.append(i)

            return temp

        else:

            # Add onto button the buttons that inherit from it
            for i in recursive_read(lines[1:index+1]):

                # Add to whether global or local
                if i.name.count('*') != 0:
                    button.addGlobal(i)
                else:
                    button.addLocal(i)

            temp = [button]

            # Carry on the function
            for i in recursive_read(lines[index+1:]):
                temp.append(i)

            return temp


class _button:
    '''
    Used to define buttons and keep the structure
    
    attributes:-
        name : str : The name of the button
        time : int : Time to delay after pressed
        globals: {str:__button} : Once button is pressed is this button still visable
        locals: {str:__button} : Once button is pressed the button will not be viewable
    '''
    def __init__(self, name, time):
        '''
        Creates a blank button.

        params:-
            name : str : the name of the button
            time : int : amount of time to delay after clicking the button
        returns:-
            None
        '''
        self.name = name
        self.time = time
        self.globals = []
        self.locals = []

    
    def __str__(self):
        '''
        Creates a string and recursively call the globals and locals.

        params:-
            None
        returns:-
            str : A recursivly called string
        '''
        tempglobals = []
        templocals = []

        # Recursivly gets all the strings of the other buttons
        for i in self.globals:
            tempglobals.append(str(i))
        for i in self.locals:
            templocals.append(str(i))

        # Converts them to a string
        globalsstr = ''
        for i in tempglobals:
            globalsstr += i + '\n'

        localsstr = ''
        for i in templocals:
            localsstr += i + '\n'

        return '\nName: ' + self.name + '\nGlobals: {' + globalsstr + '}\nLocals: {' + localsstr + '}'


    def addLocal(self, button):
        '''
        Adds a local button to the button of which this is called for

        params:-
            button : _button : the button to be added to locals
        returns:-
            None
        '''
        self.locals.append(button)

    
    def addGlobal(self, button):
        '''
        Adds a global button to the button of which this is called for

        params:-
            button : _button : the button to be added to globals
        returns:-
            None
        '''
        self.globals.append(button)
