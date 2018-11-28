from subprocess import list2cmdline

ipython_instance=get_ipython()

def background(*args):
	if not isinstance(args,str):
                args = list2cmdline(args)
	job_manager_instance.new(ipython_instance.system,args)

def runind(list):
	from subprocess import Popen,DEVNULL
	p = Popen(list, shell=False,stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL, close_fds=True,start_new_session=True)



