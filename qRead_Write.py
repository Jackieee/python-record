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
# Q区的读操作
def qRead(byte,bit):
    data=plc.read_area(0x82,0,byte,1)
    print(get_bool(data,0,bit))
# Q区的写操作
def qWrite(byte,bit,value):
    data=plc.read_area(0x82,0,byte,1)#read_area的SIZE参数，这里默认位一个字节
    set_bool(data,0,bit,value)
    plc.write_area(0x82,0,byte,1)

if __name__=='__main__':
   plc_connect('10.228.142.106',0,3)
   qRead(0,0)
   qWrite(0,0,True)
   plc_disconnect()
