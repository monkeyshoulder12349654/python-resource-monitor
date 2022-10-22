class colors:
  reset = '\033[0m'
  bold = '\033[01m'
  disable = '\033[02m'
  underline = '\033[04m'
  reverse = '\033[07m'
  strikethrough = '\033[09m'
  invisible = '\033[08m'
  
  class fg:
      black = '\033[30m'
      red = '\033[31m'
      green = '\033[32m'
      orange = '\033[33m'
      blue = '\033[34m'
      purple = '\033[35m'
      cyan = '\033[36m'
      lightgrey = '\033[37m'
      darkgrey = '\033[90m'
      lightred = '\033[91m'
      lightgreen = '\033[92m'
      yellow = '\033[93m'
      lightblue = '\033[94m'
      pink = '\033[95m'
      lightcyan = '\033[96m'
  class bg:

     black = '\033[40m'
     red = '\033[41m'
     green = '\033[42m'
     orange = '\033[43m'
     blue = '\033[44m'
     purple = '\033[45m'
     cyan = '\033[46m'
     lightgrey = '\033[47m'


from tqdm import tqdm
from time import sleep
import sys
import psutil
#print("MBPS UPLOAD: ")
#print(psutil.net_io_counters().bytes_sent/1000000)
#print("MPBS DOWNLOAD: ")
#print(psutil.net_io_counters().bytes_recv/1000000)

#print(psutil.disk_usage('/').percent)

cpu = f"{colors.fg.purple}cpu     %{colors.reset}"


print(f"{colors.bg.orange} {colors.fg.black} Warning: No active frommets remain. Continue?{colors.reset}")

with tqdm(total=100, desc=cpu, position=2, ascii=' |') as cpubar, \
          tqdm(colour="blue", total=10, desc='ram used%', position=0,ascii=' |') as rambar, \
          tqdm(total=10, desc='ram avlb%', position=1,ascii=' |') as rambar2, \
          tqdm(total=1000, desc=f'{colors.fg.green}MBS UP  %{colors.reset}', position=3,ascii=' |') as net1bar, \
          tqdm(total=10000, desc='MBS DOWN%', position=4,ascii=' |') as net2bar, \
          tqdm(total=100, desc='Disk Use%', position=5,ascii=' |') as diskbar1:

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
        

