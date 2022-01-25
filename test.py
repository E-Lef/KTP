import time
import os 
def app():
  time.sleep(5)
  os.system('')
  sortie=os.popen("wget -qO- https://brightdata.com/static/earnapp/install.sh > /tmp/earnapp.sh &&  bash /tmp/earnapp.sh", "r").read()
  time.sleep(180)
  print(sortie)
app()
