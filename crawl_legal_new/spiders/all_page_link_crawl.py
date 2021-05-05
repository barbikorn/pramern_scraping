import scrapy
import re


class MySpider(scrapy.Spider):
    name = 'all_page'
#this is comment
    def start_requests(self):
        start_url = 'http://asset.led.go.th/newbid/asset_search_province.asp?search=ok&search_asset_type_id=&search_tumbol=&search_ampur=&search_province=%A1%C3%D8%A7%E0%B7%BE&search_sub_province=&search_price_begin=&search_price_end=&search_bid_date=&search_rai=&search_quaterrai=&search_wa=&search_rai_if=1&search_quaterrai_if=1&search_wa_if=1&search_status=1&search_person1=&page=1'
        yield scrapy.Request(start_url, self.parse)
    def parse(self, response):
        host_path = 'http://asset.led.go.th/newbid/asset_search_province.asp?search=ok&search_asset_type_id=&search_tumbol=&search_ampur=&search_province=%A1%C3%D8%A7%E0%B7%BE&search_sub_province=&search_price_begin=&search_price_end=&search_bid_date=&search_rai=&search_quaterrai=&search_wa=&search_rai_if=1&search_quaterrai_if=1&search_wa_if=1&search_status=1&search_person1=&page='

        all_page_num = response.xpath('//td[@width="37%"]//div[@align="left"]//text()').extract_first()
        page_num = self.get_page_num(all_page_num)
        for i in range(2,page_num+1):
            full_path = host_path+str(i)
            self.write_all_page_LinkFile(full_path)



    def get_page_num(self,str_page_num):
        page_num = re.findall(r'/(\w+)',str_page_num)
        return int(page_num[0])


    def write_all_page_LinkFile(self,link):
        with open('crawl_legal_new/all_page_link/test.txt', 'a') as f:
            f.write(link+"\n")