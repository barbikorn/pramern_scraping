import os.path
from os import path
import re
from datetime import date
def parse_key_value(arr):
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
        return [key,value]



def connect_list_to_csv(arr1,arr2):
    newstr = ""
    for i in arr1 :
        i = i.rstrip()
        newstr = newstr+i+","
    for i in arr2 :
        i = i.rstrip()
        newstr = newstr+i+","
    newstr = newstr+"\n"
    return newstr

def write_data_to_file(key,value):
    today = date.today()
    date_folder = today.strftime("%d%m%y")
    
    host_folder = 'storage/'+date_folder+'/Page_strorage/'
    if not(path.exists(host_folder):
            os.makedirs(host_folder)
    file_path= host_folder+'all_data.txt'
    with open(file_path, 'a') as f:
        if os.stat(file_path).st_size == 0 :
            f.write(key+"\n")
    
        f.write(value+"\n")

def get_page_num(str_page_num):
    page_num = re.findall(r'/(\w+)',str_page_num)
    return page_num


def read_link_file_to_list(file_name):
    with open(file_name) as f:
        urls = f.readlines()
    return urls


# newlist = read_link_file_to_list("crawl_legal_new/all_page_link/test.txt")

# print(newlist)

arr = ['\r\n\t\t\t\t\t\t\t\t\t\t\t\t\tจำนวน ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tไม่มี\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
 ' บาท\r\n\t\t\t\t\t\t\t\t\t\t',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\tจำนวน \r\n                       \r\n                                                                   ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   2,901,300.00\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    บาท\r\n\t\t\t\t\t\t\t\t\t\t',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\tจำนวน \r\n                                                                   ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   6,769,700.00',
 ' บาท\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\tจำนวน \r\n                                                                   ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tไม่มี\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    บาท\r\n\t\t\t\t\t\t\t\t\t\t']
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


# print(newarr)

#ลบคำว่าจำนวนกับบาท
def delete_notuse_chr_from_price(arr):
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


def find_hash_and_bin(deednum):  
        h = str(hash(deednum))     # obtain its hash
        folder_name =     h[-3:]
        image_name = h[:-3]
        
        return folder_name,image_name


#save image create hash from deed no. use it as image name and folder name  

def save_image(self,deed_num,pic_path):
        today = date.today()
        date_folder = today.strftime("%d%m%y")
        host_folder = 'storage/'+date_folder+'/Page_strorage/'
        folder_name,image_name = self.find_hash_and_bin(deed_num)
        folder_name = host_folder + folder_name
        if not(path.exists(folder_name)):
            os.makedirs(folder_name)
        full_page_path = folder_name+image_name
        
        # all_file_name = host_folder + folder_name+"/"+image_name
        urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", full_img_path)

def save_data_to_csv():

def save_page(page_html,deed_num):

        today = date.today()
        date_folder = today.strftime("%d%m%y")
        host_folder = 'storage/'+date_folder+'/Page_strorage/'
        folder_name,page_name = find_hash_and_bin(page_html)
        folder_name = host_folder + folder_name
        if not(path.exists(folder_name)):
            os.makedirs(folder_name)
        full_page_path = folder_name+page_name
        
        # all_file_name = host_folder + folder_name+"/"+image_name
        with open(full_page_path, 'a') as f:
            f.write(page_html)


# save_page("head","ส.5943")








# data = 'หน้าที่ 1/129'

# print(int(get_page_num('หน้าที่ 1/129')[0]))


# test = parse_key_value(['\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'ศาล ',
#  ' ล้มละลายกลาง\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t',
#  'คดีหมายเลขแดงที่ ',
#  'ล.11986 / 2550\r\n\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'โจทก์ ',
#  'ธ.กรุงเทพ',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'จำเลย ',
#  'นายบุญเลิศ  อัจฉริยปัญญา',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'ประเภททรัพย์ ',
#  ' ที่ดินว่างเปล่า\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'ที่ดิน ',
#  ' โฉนดเลขที่\xa036797\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t',
#  'เนื้อที่',
#  '\xa021\xa0ไร่\xa01\xa0งาน\xa036\xa0ตร.วา/ตร.ม.\r\n\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'เลขที่ ',
#  ' -\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'แขวง/ตำบล ',
#  ' สองสลึง\r\n\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'เขต/อำเภอ ',
#  ' แกลง\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'จังหวัด ',
#  ' ระยอง\r\n\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t\t\t',
#  'ผู้ถือกรรมสิทธิ์',
#  '\xa0\xa0นายบุญเลิศ  อัจฉริยปัญญา\r\n\t\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'ติดต่อ สำนักงานบังคับคดี/กอง',
#  '\xa0ล้มละลาย 1\xa0\r\n\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'โทรศัพท์',
#  '\xa0028814382  \r\n\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'เจ้าของสำนวน',
#  ' ลฎาภา  แสงโพธิ์ และ พงศ์พญาเดโช  อู้สกุลวัฒนา\r\n\t\t\t\t\t\t\t\t\t\t',
#  '\r\n\t\t\t\t\t\t\t\t\t\t',
#  'สถานที่จำหน่าย',
#  ' จำหน่ายนัดที่ 1-4 ณ อาคารอสีติพรรษ กรมบังคับคดี  เลขที่ 189/1 ถนนบางขุนนนท์ แขวงบางขุนนนท์ เขตบางกอกน้อย  กรุงเทพมหานคร  เวลา 9.00  \r\n\t\t\t\t\t\t\t\t\t\t']

# )
# print(len(test[0]))
# test = connect_list_to_csv(test[0],test[1])
# write_data_to_file(test,test)