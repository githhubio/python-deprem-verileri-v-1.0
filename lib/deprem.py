import requests
from bs4 import BeautifulSoup
import time

url = "https://deprem.afad.gov.tr/last-earthquakes.html"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

gelen_veri = soup.find_all("table",{"class":"content-table"})
gelen_veri2 = soup.find_all("td")

depremzamanı = (gelen_veri2[0].contents [len(gelen_veri2[0].contents)-2])


def deprep():# anlık verileri sadece bir kere yazar
 print("turkiye son 100 deprem data=")
 print("****************************************************")
 print(gelen_veri)
 print("****************************************************")
 print("veri boyutu: ",len(gelen_veri))

def sondepreptarih():# anlık son deprem tarihini ve saatini yazar
 print("turkiye son deprem zamanı data=")
 print("****************************************************")
 print(depremzamanı)
 print("****************************************************")

def deprepolcer(xzamanbekle):#5sn de bir verileri yeniler
 while(True):
   time.sleep(xzamanbekle)
   print("turkiye son 100 deprem data=")
   print("****************************************************")
   print(gelen_veri)
   print("****************************************************")
   print("veri boyutu: ",len(gelen_veri))
