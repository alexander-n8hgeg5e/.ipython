from __future__ import print_function
from IPython.core.magic import register_line_magic
# This code can be put in any Python module, it does not require IPython
# itself to be running already.  It only creates the magics subclass but
# doesn't instantiate it yet.
from IPython.core.magic import (Magics, magics_class, line_magic)

# The class MUST call this class decorator at creation time
@magics_class
class MyMagics(Magics):
	@line_magic
	def bg(self,line):
		"my line magic"
		print(line)
		background(line)

	@line_magic
	def rind(self,line):
		from shlex import split
		"my line magic"
		l=split(line)
		print(l)
		runind(l)

# In order to actually use these magics, you must register them with a
# running IPython.  This code must be placed in a file that is loaded once
# IPython is up and running:

# You can register the class itself without instantiating it.  IPython will
# call the default constructor on it.
ipython_instance.register_magics(MyMagics)
