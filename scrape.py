import requests
from bs4 import BeautifulSoup 
import collections
import getopt
import sys
collections.Callable = collections.abc.Callable

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "d:o:")
domain=None
output=None
for opt, arg in opts:
    if opt in ['-d']:
        domain= arg.strip()
    elif opt in ['-o']:
        output=arg.strip() 
    else:
        print("[*] Wrong input given")
try:
    r=requests.get(f'https://crt.sh/?q={domain.strip()}')
except:
    print("[+]Error ouucred while making request. Check your Internet connection properly.")
else:
    soup=BeautifulSoup(r.content,'html.parser')
    s = soup.find_all("td")
    g=open(f"{output}","w")
    for i in s:
        if (domain in i.text) and not("*" in i.text) and not("Match: ILIKE" in i.text):
            print(i.text)
            g.write(f"{i.text}\n")
    g.close()
        
