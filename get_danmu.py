import socket
import re

#房间号
id = 4015880
mslist=[]
#主进程flag，用来统一退出
ison = True

#斗鱼报文格式，参看官方手册
def sendmsg(sock,msgstr) :
    msg=msgstr.encode('utf-8')
    data_length= len(msg)+8
    code=689
    msgHead=int.to_bytes(data_length,4,'little')\
            +int.to_bytes(data_length,4,'little')+int.to_bytes(code,4,'little')
    sock.send(msgHead)
    sent=0
    while sent<len(msg):
        tn= sock.send(msg[sent:])
        sent= sent + tn



def get_daunmu(roomid):
    #基本操作
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dammu_host_name = 'openbarrage.douyutv.com'
    dammu_host = socket.gethostbyname(dammu_host_name)
    send_sock.connect((dammu_host, 8601))

    #发送登陆信息，参看手册
    msg = "type@=loginreq/username@=visitor114834/password@=1234567890123456/roomid@=%d/\x00"%roomid
    sendmsg(send_sock, msg)
    BUFSIZE = 1024
    data = send_sock.recv(BUFSIZE)
    #print(data)
    data = send_sock.recv(BUFSIZE)
    #print(data)

    print(">>>登陆信息已发送")
    #发送加入组信息
    msg = "type@=joingroup/rid@=%d/gid@=-9999/\x00"%roomid
    sendmsg(send_sock, msg)
    data = send_sock.recv(BUFSIZE)
    #print(data)
    print(">>>所在组已发送")
    print("\n\n弹幕开始啦：\r\n")
    #前期工作完成，开始接收弹幕
    while ison:
        data = send_sock.recv(BUFSIZE)
        text = re.findall(b"/txt@=.+?/", data)
        if len(text)!=0:
            #print(text[0][6:][:-1].decode("utf-8"))
            try:
                mslist.append(text[0][6:][:-1].decode("utf-8"))
            except:
                pass
if __name__ == "__main__":
    get_daunmu(id)