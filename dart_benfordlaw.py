
import requests
from bs4 import BeautifulSoup
import math


def benfordlaw(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    a = soup.select('td')
    
    k = []
    for i in a:
        j = i.get_text()
        j = j.replace(",","")
        j = j.replace("(","")
        j = j.replace(")","")
        k.append(j)
        
    kk = []
    for i in k:
        try:
            kk.append(int(i))
        except:
            continue

    k = [int(str(i)[0]) for i in kk]
    ct = [k.count(i+1) for i in range(9)]
    tb = [len(k) * math.log10((i+2)/(i+1)) for i in range(9)]
    return ct, tb
    
