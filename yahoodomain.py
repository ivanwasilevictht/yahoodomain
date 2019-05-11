"""
#TARİH: 10/05/2019
#Saat: 15.34
#Kodlayıcı:ivanwasilevic [Şeyhmus]

"""
print(*"Yahoo Domain Sorgu")

while True:
    try:
        ques1 = input("Çekilen domainleri görüntülemek ister misiniz? [E/H]:")
        if ques1 == "E" :
            klas = open("Domainsiteleri.txt","r",encoding = "utf-8")
            oku1 = klas.read()
            print("Domainler : ")
            print(oku1)
            continue
        elif ques1 == "H":
            print(*"Program çalışıyor.... ")
            print("İşlem tamamlanmıştır.Tekrar bekleriz...")
            break
        else:
            print("Belirtilen prosedürleri seçiniz.")
            
    except:
     print(*"HATA")
     
 
import requests

class status:
    def init(self,dosyadi):
        self.dosyadi=dosyadi
        self.web_site=[line.rstrip('\n') for line in open('Domainsiteleri.txt') ]
        self.website_status(self.web_site)
    def website_status(self,web_site):
        self.web_site=web_site
        for i in self.web_site:
            if len(i)>1:
                try:
                    self.req=requests.get("http://"+i,timeout=2)
                    if(self.req.status_code==200):
                        self.status_200(i)
                    elif(self.req.status_code==404):
                        self.status_404(i)
                except requests.exceptions.RequestException as e:
                    pass
    def status_200(self,statuscode):
        self.statuscode=statuscode
        with open('200.txt','a') as t:
            t.write(self.statuscode+'\n')
    def status_404(self,statuscode):
        self.statuscode=statuscode
        with open('404.txt','a') as tk:
            tk.write(self.statuscode+'\n')
    def status_500(self,statuscode):
        self.statuscode=statuscode
        with open('500.txt','a') as bb:
            bb.write(self.statuscode+'\n')

