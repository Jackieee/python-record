import  snap7
from snap7.util import *


plc = snap7.client.Client()

# 定义Plc连接
def plc_connect(ip,rack,slot):
    plc.connect(ip,rack,slot)
    if plc.get_connected():
        print("连接成功")

# PLC断开连接
def plc_disconnect():
    plc.disconnect()

# DB块的写操作
def dbWrite(dbnum,dblength):
    data=plc.read_area(0x84,dbnum,0,dblength)
    set_int(data,0,20)
    set_bool(data,2,0,False)
    set_dword(data,4,1000)
    set_real(data,8,11.3)
    set_int(data,12,99)
    plc.write_area(0x84,dbnum,0,data)

if __name__=='__main__':
   plc_connect('10.228.140.46',0,3)
   dbWrite(298,14)
   plc_disconnect()
