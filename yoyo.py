import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)


def pumpeth(sc):
    with open('/root/Desktop/rebase/pumpeth.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/pumpeth.json', 'w') as file:
      file.write(filedata)
  
    s.enter(30, 1, commit, (s,))
    

def commit(sc):
    print('Commit')
    subprocess.call(['/root/Desktop/rebase/autocommit.sh'])
  
    s.enter(30, 1, pumpeth, (s,))
