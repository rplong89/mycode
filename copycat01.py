#!/usr/bin/env python3
#Need to add modules so i can call their functions
import shutil
import os
# Force working directory
os.chdir('/home/student/mycode/')
#Copy a file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
#Copy a whole directory
shutil.copytree('5g_research/', '5g_research_backup/')

