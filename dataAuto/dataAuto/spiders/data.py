from asyncio.windows_events import NULL
from types import NoneType
import scrapy
import psycopg2

conn = psycopg2.connect(host= 'localhost',database = 'Autoscout24',user = 'postgres',password = '12345')
cur = conn.cursor()

# https://www.autoscout24.com/lst/bmw?fregfrom=2018&fregto=2022&mmmv=47%7C%7C%7C%2C70%7C%7C%7C&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=1jx1g3rgegh 
# response.css('div.ListItem_header__uPzec  ::text').extract() sayfadaki araba listesi temizlenecek sekilde geliyor
# response.css('div.VehicleDetailTable_container__mUUbY ::text').extract() sayfadaki tum araba km model
# response.css('span[style="grid-area:address"] ::text').extract() tum yerler private haric
# response.css('p.Price_price__WZayw ::text').extract() sayfadaki tum  araba fiyatlari

class DataSpider(scrapy.Spider):
    name = 'data'
    # start_urls = ['https://www.autoscout24.com/lst/bmw?fregfrom=2018&fregto=2022&mmmv=47%7C%7C%7C%2C70%7C%7C%7C&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=1jx1g3rgegh']
    start_urls=['https://www.autoscout24.com/lst/bmw?fregfrom=2018&fregto=2022&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=86yr7rbaeq','https://www.autoscout24.com/lst/mercedes-benz?fregfrom=2018&fregto=2022&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=1guq5i7iz6p','https://www.autoscout24.com/lst/toyota?fregfrom=2018&fregto=2022&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=1l96md7gst7']
    def parse(self, response):
        hrefs=response.css('a[class="ListItem_title__znV2I Link_link__pjU1l"]')
        # hrefs=response.css('div.ListItem_header__uPzec')
        for href in hrefs:
            ek=href.css('::attr(href)').get()
            yeni_url=response.urljoin(ek)
            yield scrapy.Request(yeni_url,callback=self.detail)
        next=response.css('a[aria-label="Go to next page"] ::attr(href)')

        if next:
            url=response.urljoin(next.get())
           
            yield scrapy.Request(url,callback=self.parse)
    def detail(self,response):
        brand_model=response.css('span[class="css-a36h5"] ::text').get()+response.css('span[class="css-1mhe8d errr7t00"] ::text').get()+response.css('div.css-l08njs ::text').get()
        brand_model=brand_model.encode("ascii","ignore")
        brand_model=brand_model.decode()
        plate=response.xpath('//*[@id="__next"]/div/div/main/div[6]/div[3]/div/div[2]/div/dl/dd[6]/text()').get()
        if type(plate)==NoneType:
            plate="No License Plate"
        milage=response.css('div.VehicleOverview_itemText__V1yKT ::text').get()
        price=response.css('span.StandardPrice_price__X_zzU ::text').get()
        price=price.encode("ascii","ignore")
        price=price.decode()
        price=price.split(".")[0]
        price=price.strip()
        year=response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[3]/div[2]/div[3]/div[4]/text()').get()
        province=response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[2]/a/text()').get().split(',')[0]
        image= response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[1]/div/div/div[1]/div[1]/div/div[1]/picture/img/@src').get()
        yield{"Marka":brand_model,"Plaka":plate,"Kilometre":milage,"Fiyat":price,"Model":year,"Yer":province,"Resim":image}

        cur.execute("insert into cars (brand_model,plate,km,year,price,province,image) values (%s, %s, %s,%s, %s, %s, %s);",(brand_model,plate,milage,year,price,province,image))
        conn.commit()
        

        
        

        
