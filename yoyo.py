import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)


def pumpeth(sc):
    print('Enter')
    with open('/root/Desktop/peth/peth.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/peth/peth.json', 'w') as file:
      file.write(filedata)
  
    s.enter(5, 1, commit, (s,))
    

def commit(sc):
    print('Commit')
    subprocess.call(['/root/Desktop/peth/auto.sh'])
    print('Done')
  
    s.enter(30, 1, pumpeth, (s,))


s.enter(5, 1, pumpeth, (s,))
s.run()
