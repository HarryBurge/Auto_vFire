#!/usr/local/bin/python3
'''
This is the main API of which is used to use the whole Auto_vFire
library.
'''

__Authour__ = 'Harry Burge'
__DateCreated__ = '04/02/2020'
__LastUpdated__ = '04/02/2020'

# Imports
from bin.insturctor import compiler
import sys

def main_compile(path):

    file = open(path, 'r')
    lines = file.read().split('\n')
    file.close()
    if lines[-1] == '':
        del lines[-1]
    if len(lines) == 0:
        raise RuntimeError('File to compile is empty')

    compiler.compile(lines)


def main(args):

    del args[0]
    
    if len(args) != 0:

        if args[0] in ['-c','-C','--compile','--Compile'] and len(args)==2:
            if args[1].split('.')[-1] == 'txt':
                main_compile(args[1])
            else:
                raise RuntimeError('The file to be compiled isn\'t a text file')

        else:
            raise RuntimeError('Please select an option, with correct passed info.\nPlease refer to -hlp for more info')
    else:
        raise RuntimeError('No arguments passed.\nPlease refer to -hlp for more info')


if __name__ == '__main__':
    main(sys.argv)