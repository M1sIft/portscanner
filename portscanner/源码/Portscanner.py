# -*- coding: utf-8 -*-
from socket import *
import threading
import time

lock = threading.Lock()
opennum = 0
threads = []
remote_server_ip = input("please input the host:")
ip = gethostbyname(remote_server_ip)


def portScanner(host, port):
    global opennum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        s.send(b'Primal Security')  # 传输的数据类型是bytes
        banner = s.recv(1000)
        lock.acquire()
        opennum += 1
        print('[+] %d open' % port)
        print('[-]banner is :%s' % bytes.decode(banner))  # 将数据从bytes转换为string型
        lock.release()
        s.close()
    except:
        pass
    # except Exception as e:
    #    print(e)


def main():
    setdefaulttimeout(3)
    for p in range(1, 65535):
        t = threading.Thread(target=portScanner, args=(ip, p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % opennum)
    print('100秒后控制台将关闭')
    time.sleep(100)  # 设置控制台关闭时间


if __name__ == '__main__':
    main()
