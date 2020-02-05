from subprocess import list2cmdline
import subprocess
sp=subprocess
import re
import sys
import os
from pprint import pprint,pformat
# quick path set

def spp(path,p=0):
    # sys path prepend
    path=os.path.expandvars(path)
    path=os.path.expanduser(path)
    sys.path.insert(p,path)
    pprint(sys.path)


import importlib
il=importlib


ipython_instance=get_ipython()

def background(*args):
	if not isinstance(args,str):
                args = list2cmdline(args)
	job_manager_instance.new(ipython_instance.system,args)

def runind(list):
	from subprocess import Popen,DEVNULL
	p = Popen(list, shell=False,stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL, close_fds=True,start_new_session=True)



