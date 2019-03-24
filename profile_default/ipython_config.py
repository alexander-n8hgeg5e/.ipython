c = get_config()
c.TerminalInteractiveShell.autoindent=True
c.TerminalInteractiveShell.autocall=0
c.TerminalInteractiveShell.automagic=True
#c.TerminalIPythonApp.log_level='DEBUG'
c.IPCompleter.jedi_compute_type_timeout=10000
c.TerminalInteractiveShell.autocall=0
#c.TerminalInteractiveShell.highlighting_style='native'
#c.TerminalInteractiveShell.colors='neutral'
c.TerminalInteractiveShell.color_info=False
c.TerminalInteractiveShell.editing_mode = 'vi'
c.TerminalInteractiveShell.space_for_menu=20
c.HistoryManager.db_log_output=True


f=open( "/tmp/background", mode='wt+' )
data=f.readline().strip()
if data == 'light':
    c.TerminalInteractiveShell.colors='LightBG'
elif data == 'dark':
    c.TerminalInteractiveShell.colors='Neutral'
else:
    c.TerminalInteractiveShell.colors='Linux'
    f.seek(0);
    f.writelines("Neutral")
    f.close()
