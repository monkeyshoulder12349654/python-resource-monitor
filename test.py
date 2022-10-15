
#import psutil
#psutil.cpu_percent()
#psutil.virtual_memory()
#dict(psutil.virtual_memory()._asdict())
#psutil.virtual_memory().percent
#79.2
#psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
#20.8

#from __future__ import print_function
#import psutil
#print(psutil.cpu_percent())
#print(psutil.virtual_memory())  # physical memory usage
#print('memory % used:', psutil.virtual_memory()[2])


#sys.stdout.write("\r{0}".format(psutil.virtual_memory()[3]/1000000000))
 #       sys.stdout.write("\r\n")
  #      sys.stdout.flush()
from tqdm import tqdm
from time import sleep
import sys
import psutil





with tqdm(total=100, desc='cpu     %', position=2) as cpubar, tqdm(total=100, desc='ram used%', position=0) as rambar, tqdm(total=100, desc='ram avlb%', position=1) as rambar2:
    while True:
        
        rambar2.n=100*round((psutil.virtual_memory().available/psutil.virtual_memory().total),2)
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        rambar2.refresh()
        cpubar.refresh()
        
        #print('memory used:', , 'GB')
        #print('memory available:', psutil.virtual_memory()[1]/1000000000, 'GB')

        sleep(0.5)
        

