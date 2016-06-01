'''
Created on Jun 1, 2016

@author: jiajyang
'''
import unittest
import cc_base
import cc_process_line
import cc_process_file

class Test(unittest.TestCase):

    def test_proc_line(self):
        line1 = '4    4    13    91    25    ./src/lsd_client_conn_mgr.c(92): lsd_cc_mgr_client_get'
        cc_function = cc_process_line.proc_line(line1)
        self.assertEqual(cc_function.cc_modified, 4, 'cc_function.cc_modified')
        self.assertEqual(cc_function.cc_original, 4, 'cc_function.cc_original')
        self.assertEqual(cc_function.func_file, 'lsd_client_conn_mgr.c', 'cc_function.func_file')
        self.assertEqual(cc_function.func_name, 'lsd_cc_mgr_client_get', 'cc_function.func_name')
        pass
    def test_proc_file(self):
        testfile = "test.txt"
        cc_files = cc_process_file.proc_result_file(testfile)
        
        counter = 0
        for sf in cc_files:
            counter+=1
            if (counter == 1):
                self.assertEqual(sf.filename, 'lsd_debug.c', 'filename wrong at 1')
            if (counter == 2):
                self.assertEqual(sf.filename, 'lsd_update_list_mgr.c', 'file name wrong at 2')
                for func in sf.func_list:
                    if (func.func_name == 'lsd_ul_mgr_pkg_upd'):
                        self.assertEqual(func.get_modifiedcc(), 26, "error at lsd_ul_mgr_pkg_upd")
                        self.assertEqual(func.get_originalcc(), 37, "error at lsd_ul_mgr_pkg_upd")
        self.assertEqual(counter, 2, 'loop counter')
        
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()