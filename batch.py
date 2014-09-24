#!/home/zywang/Enthought/Canopy_64bit/User/bin/python
from SimpleParallel import *
import sys
__author__ = 'zywang'
# This script is used to replace batch.pl before
file1=sys.argv[1]
cmdlist=readlist(file1)
computer=LocalCruncher()
computer.runbatch_and_wait(cmdlist)
