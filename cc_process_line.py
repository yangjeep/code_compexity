'''
Functions to read file and process files into classes 
Created on Jun 1, 2016

@author: jiajyang
'''
import re
from cc_base import cc_function

def proc_line(line):
    # Split string
    splited_line = line.split()

    # parse all the numbers
    numbers = re.findall("[-+]?\d+[\.]?\d*", line) 

    modified = int(numbers[0])
    traditional = int(numbers[1])
    num_statements = int(numbers[2])
    first_line = int(numbers[3])
    loc_in_func = int(numbers[4])

    # Get file name
    file_name = splited_line[5]
    last = file_name.find("(")
    start = file_name.rfind("/")
    file_name = file_name[start + 1:last]

    # Get function name
    func_name = splited_line[6]
    
    retval = cc_function(func_name, file_name, modified, traditional, num_statements, loc_in_func, first_line)
    return retval

    
    