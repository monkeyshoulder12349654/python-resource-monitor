
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
#print("MBPS UPLOAD: ")
#print(psutil.net_io_counters().bytes_sent/1000000)
#print("MPBS DOWNLOAD: ")
#print(psutil.net_io_counters().bytes_recv/1000000)

#print(psutil.disk_usage('/').percent)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

with tqdm(total=100, desc='cpu     %', position=2, ascii='░▒█') as cpubar, \
          tqdm(total=10, desc='ram used%', position=0,ascii=' #') as rambar, \
          tqdm(total=10, desc='ram avlb%', position=1,ascii='░▒█') as rambar2, \
          tqdm(total=100, desc=f'{bcolors.OKGREEN}MBS UP  %{bcolors.ENDC}', position=3,ascii='░▒█') as net1bar, \
          tqdm(total=1000, desc='MBS DOWN%', position=4,ascii='░▒█') as net2bar, \
          tqdm(total=100, desc='Disk Use%', position=5,ascii='░▒█') as diskbar1:

    while True:
        
        rambar2.n=round(10*(psutil.virtual_memory().available/psutil.virtual_memory().total),2)
        rambar.n=round((psutil.virtual_memory().percent/10),2)
        cpubar.n=psutil.cpu_percent()
        net1bar.n=psutil.net_io_counters().bytes_sent/1000000
        net2bar.n=psutil.net_io_counters().bytes_recv/1000000
        diskbar1.n=psutil.disk_usage('/').percent
        
        rambar.refresh()
        rambar2.refresh()
        cpubar.refresh()
        net1bar.refresh()
        net2bar.refresh()
        diskbar1.refresh()
        #print('memory used:', , 'GB')
        #print('memory available:', psutil.virtual_memory()[1]/1000000000, 'GB')

        sleep(0.5)
        

