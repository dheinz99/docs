import os
hostname = "google.com"
response = os.system("ping -c 1 www.wynnlasvegas.com")

if response == 0:
    print (hostname,  'is up!')
else:
    print (hostname, 'is down!')
    abs
    