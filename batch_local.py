#!/home/zywang/Enthought/Canopy_64bit/User/bin/python
import sys

from SimpleParallel import *

__author__ = 'zywang'
# This script is used to replace batch.pl before
file1=sys.argv[1]
ncpu=int(sys.argv[2])
cmdlist=readlist(file1)
computer=ComputingHost(ncpu=ncpu)
computer.runbatch_and_wait(cmdlist)
