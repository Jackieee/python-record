import  snap7

plc = snap7.client.Client()

def plc_connect(ip,rack,slot):
    plc.connect(ip,rack,slot)
    if plc.get_connected():
        print("连接成功")
if __name__=='__main__':
    plc_connect('10.228.140.46',0,3)
