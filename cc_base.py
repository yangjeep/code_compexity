'''
Base structure regarding a function in a file
Created on Jun 1, 2016

@author: jiajyang
'''

class cc_function(object):
    '''
    classdocs
    '''
    func_name = ''
    func_file = ''
    cc_modified = 0
    cc_original = 0
    cc_num_statement = 0
    func_loc = 0
    cc_firstline = 0
    def __init__(self, name, filename, modifiedcc, originalcc, num_statement, loc, firstline):
        '''
        Constructor
        '''
        self.func_name = name
        self.func_file = filename
        self.cc_modified = modifiedcc
        self.cc_original = originalcc
        self.cc_num_statement = num_statement
        self.func_loc = loc
        self.cc_firstline = firstline
    
    def get_modifiedcc(self):
        return self.cc_modified
    def get_originalcc(self):
        return self.cc_original
    def get_loc(self):
        return self.func_loc
    def get_filename(self):
        return self.func_file    

class cc_srcfile(object):
    '''
    classdocs
    '''
    filename = ''
    func_list = []

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.filename = filename
    def add_func(self, ccfunc):
        self.func_list.append(ccfunc)
        
        