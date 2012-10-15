'''
Created on 12.10.2012

@author: cbalea
'''

from subprocess import Popen
import glob
import time
 
tests = glob.glob('tests/test*.py')
tests += glob.glob('tests/subtests/test*.py')


total_test_suites = len(tests)
parallel_tests = total_test_suites
#print total_test_suites

j=0

while j < total_test_suites:
    processes = []
    for i in xrange(parallel_tests):
        processes.append(Popen('nosetests %s --with-xunit --xunit-file=testresults%i.xml' %(tests[j], j), shell=True))
        j+=1
    
    for process in processes:
        process.wait()
        time.sleep(1)
        


#processes = []
#i=0
#for test in tests:
#    i+=1
#    processes.append(Popen('nosetests %s --with-xunit --xunit-file=testresults%i.xml' %(test, i), shell=True))
# 
#for process in processes:
#    process.wait()
