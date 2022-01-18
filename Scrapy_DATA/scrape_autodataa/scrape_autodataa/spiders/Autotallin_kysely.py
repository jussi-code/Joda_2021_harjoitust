import scrapy
from time import time,ctime



class QuoteSpider(scrapy.Spider):
    name = "autodata_kysely"




    def start_requests(self):
        
        urls=[]
        merkit=['audi','bmw','nissan']#['skoda','toyota','volkswagen']#
        mallit=[['a3','a4','a5'],['1-sarja','3-sarja','5-sarja'],['micra','qashqai','qashqai-2']]#[['fabia','octavia','superb'],['auris','avensis','corolla'],['golf','passat','polo']]#[['a3','a4','a5'],['1-sarja','3-sarja','5-sarja'],['micra','qashqai','qashqai-2']]#,['fabia','octavia','superb'],['auris','avensis','corolla'],['golf','passat','polo']]
    
    

        for i in range(len(merkit)):
            for j in range(len(mallit[i])):
                url1='https://www.autotalli.com/vaihtoautot/listaa/'+merkit[i]+'/'+mallit[i][j]+'/polttoaine/bensiini/vuosimalli_min/2005/max_osumia/100/jarjestys/current_price:asc'
                url2='https://www.autotalli.com/vaihtoautot/listaa/'+merkit[i]+'/'+mallit[i][j]+'/sivu/2/polttoaine/bensiini/vuosimalli_min/2005/max_osumia/100/jarjestys/current_price:asc'
                url3='https://www.autotalli.com/vaihtoautot/listaa/'+merkit[i]+'/'+mallit[i][j]+'/sivu/3/polttoaine/bensiini/vuosimalli_min/2005/max_osumia/100/jarjestys/current_price:asc'
                urls.append(url1)
                urls.append(url2)
                urls.append(url3)
                url1=""
                url2=""
                url3=""
        
        start_urls = urls#['https://www.autotalli.com/vaihtoautot/listaa/audi/a3/polttoaine/bensiini/vuosimalli_min/2010/max_osumia/100/jarjestys/current_price:asc','https://www.autotalli.com/vaihtoautot/listaa/audi/a4/polttoaine/bensiini/vuosimalli_min/2010/max_osumia/100/jarjestys/current_price:asc',]

        #Yllä oleva url lista käydään läpi yksitellen ja Responsea käsitellään Parse funktiolla joka on määritelty alempana
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            #jakaja = re.compile("\w+")
            #tulos=jakaja.findall(url)
            #automerkki=tulos[6]
            #automalli=tulos[7]

            


    #response käsitellään tällä funktiolla niin että sivun kustakin carsListItemDetailsContainer:sta poimitaan kiinnostavat arvot, loppuun lisätään vielä response.url
    def parse(self, response):
        
        for car in response.css('.carsListItemDetailsContainer'):
            #self.logger.info("data from: {}".format(response.url))
            
            yield {
            
                'OTSIKKO': car.css('.carsListItemNameLink::text').get(),
                'VM.': car.css('.usedCarsListItemCarModelYear').css('.carsListItemCarBottomContainerItem::text').get(),
                'AJETTU': car.css('.usedCarsListItemCarMeterReading').css('.carsListItemCarBottomContainerItem::text').get(),
                'HINTA': car.css('.carsListItemCarPrice').css('.carsListItemCarBottomContainerItem::text').get(),
                'URL':"{}".format(response.url),
                'LINKKI ILMOITUKSEEN': car.css('.carsListItemNameLink::attr(href)').extract()[0],
                'HAUN AIKA':"{}".format(ctime(time()))
    
            }




