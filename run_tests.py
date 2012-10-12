'''
Created on 12.10.2012

@author: cbalea
'''

from subprocess import Popen
import glob
 
tests = glob.glob('tests/test*.py')
tests += glob.glob('tests/subtests/test*.py')

processes = []
i=0
for test in tests:
    i+=1
    processes.append(Popen('nosetests %s --with-xunit --xunit-file=testresults%i.xml' %(test, i), shell=True))
 
for process in processes:
    process.wait()
