'''
Created on 12.10.2012

@author: cbalea



'''

from subprocess import Popen
import glob
import time
 
tests = glob.glob('tests/test*.py')
#tests += glob.glob('tests/subtests/test*.py')
total_test_suites = len(tests)
processes = []
parallel_tests = 2


def start_processes(start_index, nb_of_processes):
    for i in xrange(start_index, start_index+nb_of_processes):
        print i
        try:
            processes.append(Popen('nosetests %s --with-xunit --xunit-file=testresults%i.xml' %(tests[i], i), shell=True))
        except IndexError:
            break
    for process in processes:
        process.wait()


def count_old_alive_processes(current_process):
    alive_processes=0
    for i in xrange(current_process):
        try:
            if(processes[i].poll() == None):
                alive_processes+=1
        except IndexError:
            alive_processes+=0
    return alive_processes


     

start_processes(0, parallel_tests)

j = parallel_tests
while j < total_test_suites:
    print "j=%d" %j
    alive_processes = count_old_alive_processes(j)
    print "alive processes = %d" %alive_processes
    if(alive_processes < parallel_tests):
        needed_processes = parallel_tests - alive_processes
        print "needed_processes= %d" %needed_processes
        start_processes(j, needed_processes)
        j+=1

