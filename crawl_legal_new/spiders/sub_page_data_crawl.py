
import os
import os.path
from os import path
import scrapy
import csv
import urllib.request
from datetime import date


class QuotesSpider(scrapy.Spider):
    name = "page_data"
    # custom_settings = {
    #     'DOWNLOAD_DELAY' : 'RANDOMIZE_DOWNLOAD_DELAY',
    # }
             


    def start_requests(self):
        urls = self.read_link_file_to_list('crawl_legal_new/sub_page_link/test.txt')
        # urls = [
        #     'http://asset.led.go.th/newbid/asset_open.asp?law_suit_no=%C5.11986&law_suit_year=2550&Law_Court_ID=112&deed_no=34633&addrno=-'  
        #     ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        all_price_data = response.xpath('//div[@class="col-lg-7 col-md-12 col-sm-12"]/div[@class="row"]')
        all_meta_data = response.xpath('//div[@class="card-body"]//div[@class="row"]//div[@class="card-text"]//text()').extract()

        meta = self.parse_key_value_meta(all_meta_data)
        price= self.parse_key_value_price(all_price_data)


        all_key = self.connect_list_to_csv(meta[0],price[0])
        all_value = self.connect_list_to_csv(meta[1],price[1])

        #get image and page body
        pic_path = response.xpath('//div[@id="lightgallery"]//@data-responsive').extract_first()
        pic_url = 'http://asset.led.go.th'+pic_path
        page_body = response.body
        deed_num = all_value[1]
        # self.save_image(deed_num,pic_url)
        self.save_page(deed_num,page_body)

        self.write_data_to_file(all_key,all_value)
        
#input : response 
    def parse_key_value_price(self,arr):
        key = arr.xpath('//div[@class="col-lg-8 col-md-8 col-sm-8"]//text()').extract()
        value = arr.xpath('//div[@class="col-lg-4 col-md-4 col-sm-4"]//text()').extract()
        key = self.delete_notuse_chr_from_price_value(key)
        value = self.delete_notuse_chr_from_price_value(value)

        return [key,value]

#input : lists    
    def parse_key_value_meta(self,arr):
        today = date.today()
        key = []
        value = []
        newarr = []
        index = 0
        for i in arr :
            i = i.rstrip()
            if i != "":
                newarr.append(i)
        for i in newarr:
            if index %2 == 0 :
                key.append(i)
            else :
                value.append(i)
            index+= 1
        key.append('crawl_date')
        value.append(date.today)
        return [key,value]
    
    def write_data_to_file(self,key,value):
        today = date.today()
        date_folder = today.strftime("%d%m%y")
        host_folder = 'storage/'+date_folder+'/data_storage/'
        if not(path.exists(host_folder)):
            os.makedirs(host_folder)
        file_path= host_folder+'all_data.txt'
        with open(file_path, 'a') as f:
            write = csv.writer(f)
            if os.stat(file_path).st_size == 0 :
                write.writerow(key)
        
            write.writerow(value)
# connect list and return string
    def connect_list_to_csv(self,arr1,arr2):
        return arr1+arr2


    #ลบคำว่าจำนวนกับบาท
    def delete_notuse_chr_from_price_value(self,arr):
        newarr = []
        for i in arr :
            i = i.replace("จำนวน","")
            i = i.replace("บาท","")
            i = i.replace(",","")
            i = i.replace("\r","")
            i = i.replace("\n","")
            i = i.replace("\t","")
            i = i.rstrip()
            if len(i) > 0 :
                newarr.append(i) 
        
        return newarr

    #use hash to collect image
    def find_hash_and_bin(self,deednum):  
        h = str(hash(deednum))     # obtain its hash
        folder_name = h[-3:]
        image_name = h[:-3]
        
        return folder_name,image_name
    
   #save image and page create hash from deed no. use it as image name and folder name  

    def save_image(self,deed_num,pic_url):
        today = date.today()
        date_folder = today.strftime("%d%m%y")
        host_folder = 'storage/'+date_folder+'/Page_strorage/'
        folder_name,image_name = self.find_hash_and_bin(deed_num)
        folder_name = host_folder + folder_name + "/"
        if not(path.exists(folder_name)):
            os.makedirs(folder_name)
        full_img_path = folder_name+image_name
        
        # all_file_name = host_folder + folder_name+"/"+image_name
        urllib.request.urlretrieve(pic_url, full_img_path)


    def read_link_file_to_list(self,file_name):
            with open(file_name) as f:
                urls = f.readlines()
            return urls

    def save_page(self,deed_num,page_html):

        today = date.today()
        date_folder = today.strftime("%d%m%y")
        host_folder = 'storage/'+date_folder+'/Page_strorage/'
        folder_name,page_name = self.find_hash_and_bin(page_html)
        page_name = page_name +".txt"
        folder_name = host_folder + folder_name
        if not(path.exists(folder_name)):
            os.makedirs(folder_name)
        full_page_path = folder_name+'/'+page_name
        
        # all_file_name = host_folder + folder_name+"/"+image_name
        with open(full_page_path, 'wb') as f:
            f.write(page_html)

    def check_dir_exist(dir_name):
        if  my_file.is_dir() :
            return t

  