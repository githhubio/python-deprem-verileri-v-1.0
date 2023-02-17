import requests
from bs4 import BeautifulSoup
import time

url = "https://deprem.afad.gov.tr/last-earthquakes.html"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

gelen_veri = soup.find_all("table",{"class":"content-table"})

gelen_veri2 = soup.find_all("table","td")

depremzamanı = (gelen_veri2[0].contents [len(gelen_veri2[0].contents)-2])

def depremveri():# anlık verileri sadece bir kere yazar
 print("----------------------------------------------------")
 print(gelen_veri)

def sondepreptarih():# anlık son deprem tarihini ve saatini yazar
 print("----------------------------------------------------")
 print(depremzamanı)

def deprepolcer(xzamanbekle,y):#5sn de bir verileri yeniler
 while(True):
   time.sleep(xzamanbekle)
   print("----------------------------------------------------")
   print(gelen_veri)
   print("----------------------------------------------------")
   if(y == True):# y = 1 ise veri boutu ile yaz
    print("veri boyutu: ",len(gelen_veri))

def veriboyutu(q):#gelen veri boyutunu söyler 1-veriler için 2-zaman
  if(q == 1):
    boyut = len(gelen_veri)
    print("----------------------------------------------------")
    print("veri boyutu: ",boyut)
    print("----------------------------------------------------")
    return gelen_veri
  else:
    boyut = len(gelen_veri)
    print("----------------------------------------------------")
    print("veri boyutu: ",boyut)
    print("----------------------------------------------------")
    return gelen_veri2
