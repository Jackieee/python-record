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

# M块的写操作
def mWrite(byte,bit,value):
    data=plc.read_area(0x83,0,byte,1)
    set_bool(data,0,bit,value)
    plc.write_area(0x83,0,0,data)

# M区的读操作
def mRead(byte,bit):
    data=plc.read_area(0x83,0,byte,1)
    print(get_bool(data,0,bit))

if __name__=='__main__':
   plc_connect('10.228.140.46',0,3)
   mRead(20,3)
   mWrite(20,3,True)
   plc_disconnect()
