#created by JJF3
import sys

sys.stdout = open('logfile', 'w')

# ... rest of program ...
from googlesearch import search
for url in search ("Biden" ):
    print(url)
