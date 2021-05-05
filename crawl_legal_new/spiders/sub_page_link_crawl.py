import scrapy

# สำคัญมาก!! เวลา crawlinkมาจะได้ภาษไทยซึ่งต้องเปลี่ยนเองด้วย replace เช่น ล. ห้ามลืม


class QuotesSpider(scrapy.Spider):
    name = "field_page"

    def start_requests(self):
        urls = self.read_link_file_to_list("crawl_legal_new/all_page_link/test.txt")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        host_path = 'http://asset.led.go.th/newbid/'
        self.writeLog("seconds success")
        # start_url = "http://asset.led.go.th/newbid/"
        # page = response.url.split("/")[-2]
        paths = response.xpath("//table[@class='table linkevent']").re("window.open\('(.+?)'",replace_entities=True)
        for path in paths :
            full_path = host_path+path
            #แก้ linkให้ใช้ได้โดยลบ amp;
            full_path = full_path.replace('amp;','')
            #แก้ ภาษาไทยในน link
            full_path = full_path.replace('ผบ.','%BC%BA.')
            full_path = full_path.replace('กค.','%A1%A4.')
            full_path = full_path.replace('ธ.','%B8.')
            full_path = full_path.replace('พ.','%BE.')
            full_path = full_path.replace('ฟ.','%BF.')
            full_path = full_path.replace('ม.','%C1.')
            full_path = full_path.replace('ย.','%C2.')
            full_path = full_path.replace('ล.','%C5.')
            full_path = full_path.replace('พณ.','%BE%B3.')
            full_path = full_path.replace('ลฟ.','ſ.')
            
            
            self.write_all_page_LinkFile(full_path)

        return self.writeLog('third success')
        
        # self.log(f'Saved file {filename}')
        # yield(print("paths"))
    def writeLog(self,message):
        with open('Log.txt', 'a') as f:
            f.write(message)
    
    def write_all_page_LinkFile(self,link):
        with open('crawl_legal_new/sub_page_link/test.txt', 'a') as f:
            f.write(link+"\n")   

    def read_link_file_to_list(self,file_name):
        with open(file_name) as f:
            urls = f.readlines()
        return urls


    def my_encode(self,str):
        hex(ord("http://asset.led.go.th/newbid/asset_open.asp?law_suit_no=ผบ.4774&law_suit_year=2561&Law_Court_ID=103&deed_no=65423&addrno=68/1430".encode('tis-ุ620')))

# re.search("window.open\('(.+?)'", value)