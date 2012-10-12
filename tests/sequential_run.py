'''
Created on 12.10.2012

@author: cbalea
'''

import os
import glob
 
tests = glob.glob('test*.py')
for test in tests:
    os.system('python %s' %test)