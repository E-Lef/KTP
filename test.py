import time
import os 
def app():
  time.sleep(5)
  os.system('')
  sortie=os.popen("echo lol", "r").read()
  time.sleep(180)
  print(sortie)
app()
