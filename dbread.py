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
# DB块的读操作
def dbwRead(dbnum,dblength):
    data=plc.read_area(0x84,dbnum,0,dblength)
    print(get_int(data,0))
    print(get_bool(data,2,0))
    print(get_dword(data,4))
    print(get_real(data,8))
    print(get_int(data,12))


if __name__=='__main__':
   plc_connect('10.228.140.46',0,3)
   dbwRead( 298, 14)
   plc_disconnect()
