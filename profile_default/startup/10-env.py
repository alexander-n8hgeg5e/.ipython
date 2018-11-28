import os
os.environ['PATH']=os.environ['PATH']+':'+ os.environ['HOME'] +'/bin'
ipython_instance.magics_manager.shell.run_line_magic('rehashx','')
