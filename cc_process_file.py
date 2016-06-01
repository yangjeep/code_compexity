'''
Parse given file, and gather a list of file objects (as return)
Created on Jun 1, 2016

@author: jiajyang
'''
import cc_base
import cc_process_line

def proc_result_file(txt_file_name):
    flist = []
    src_c = cc_base.cc_srcfile('')
    prev_c = cc_base.cc_function('', '', 0, 0, 0, 0, 0)
    prev_c.func_name = ''
    
    searchfile = open(txt_file_name, "r")
    for line in searchfile:
        func_c = cc_process_line.proc_line(line)
        if (func_c.func_file != prev_c.func_file):
            src_c = cc_base.cc_srcfile(func_c.func_file)
            flist.append(src_c)
        prev_c = func_c
        src_c.add_func(func_c)
    return flist   
        
        