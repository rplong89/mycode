#!/usr/bin/env python3

#Import modules, so I can use their functions
import shutil
import os

#Force working directory
os.chdir('/home/student/mycode/')

# Move some files around
shutil.move('raynor.obj', 'ceph_storage/')

#Prompt the user for a new name
xname = input('What is the new name for kerrigan.obj? ')

#Apply requested name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

