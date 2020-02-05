c = get_config()
c.TerminalInteractiveShell.autoindent=True
c.TerminalInteractiveShell.autocall=0
c.TerminalInteractiveShell.automagic=True
#c.TerminalIPythonApp.log_level='DEBUG'
c.IPCompleter.jedi_compute_type_timeout=10000
c.TerminalInteractiveShell.autocall=0
#c.TerminalInteractiveShell.highlighting_style='native'
from os import environ
envsock = environ['NVIM_LISTEN_ADDRESS']
import neovim
nvim=neovim.attach('socket',path=envsock)

try:
    if nvim.call('eval','&background')=='light':
        c.TerminalInteractiveShell.colors= 'LightBG'
    elif nvim.call('eval','&background')=='dark':
        c.TerminalInteractiveShell.colors= 'Linux'
except KeyboardInterrupt as k:
    raise k
except:
    c.TerminalInteractiveShell.colors= 'LightBG'

c.TerminalInteractiveShell.color_info=False
c.TerminalInteractiveShell.editing_mode = 'vi'
c.TerminalInteractiveShell.space_for_menu=20
c.HistoryManager.db_log_output=True
