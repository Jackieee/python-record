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
#  输入映象区的读操作
def iRead(byte,bit):
    data=plc.read_area(0x81,0,byte,1)#Size参数，这里我们定义为1个字节的长度
    print(get_bool(data,0,bit))

if __name__=='__main__':
   plc_connect('10.228.142.106',0,3)
   iRead(0,0)
   iRead(0, 1)
   iRead(0, 2)
   iRead(0, 3)
   iRead(0, 4)
   iRead(0, 5)
   iRead(0, 6)
   iRead(0, 7)

   plc_disconnect()
