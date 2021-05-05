from shapely.geometry import Point, LineString
from shapely.ops import nearest_points
import csv
from crud import Crud
import dblib



conn = dblib.connectDb( "database.ini" , "postgresql")
from_led = Crud( conn , 'from_led')


#read Database province = Bangkok and Type = "ที่เปล่า" update_template = 
select_by_province_template = select * from customer where province = %s
#find and list nearest facility

#re_data inform of array
def appraisal_land_1(re_data):
    #a = array of similar prop
    
    prop_in_bkk = gets_BKK():
    factor = []
    similar_prop = find_similar(re_data,factors)            #factor is array of factor that effect property price
    estimate_price = find_estimate(similar_prop)            #


    return estimate_price
def gets_BKK():
    return from_led.gets("province =  กรุงเทพฯ")

def read_BTS():

    return bts_station        #geometric data

def read_MRT():

    return mrt_station      

def find_nearest():
    pt_a = Point(x,y)
    ls = LineString([Point(point.x, point.y) for point in list_of_points)
    nearest_pts = [pt for pt in nearest_points(pt_a, ls)    


def appraisal_land_mul():
    #use model
    price = 0
    return price








def find_similar(re_data):
#   find 3-5 similar property 
#            nearest &     
#   1. query similar data from database 
#   2. edit and save in one array(array of similar propoty)


def find_estimate(re_data):



