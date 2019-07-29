import re
import time
import socket


def first(sock):
    res = sock.recv(250).decode('utf-8')
    sock.send('246.69.53.233\n'.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res = res.split('\n')
    return res


def which(ip):
    if ip == "215.239.98.18":
        return "1\n"
    if ip == "246.69.53.233":
        return "3\n"
    if ip == "231.205.245.44":
        return "1\n"
    if ip == "251.165.34.242":
        return "3\n"


def second(sock, first_res):
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
                   first_res[-2]).group()
    ans = which(ip)
    sock.send(ans.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res.split('\n')
    return res


def third(sock, ans):
    ans = str(ans) + "\n"
    sock.send(ans.encode('utf-8'))
    res = sock.recv(250).decode('utf-8')
    res = res.split('\n')
    return res


if __name__ == '__main__':


    port = 54782
    host = "2018shell.picoctf.com"

    # Loop over third question
    i = 1.00
    j = 2.00
    for third_ans in [float(j)/100 for j in range(110, 1501, 1)] :
      for third_ans in [i, j] :

        print("Trying", third_ans)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print("socket creation failed with error %s" % (err))
        sock.connect((host, port))

        first_res = first(sock)

        second_res = second(sock, first_res)

        third_res = third(sock, third_ans)
        print("Output : ", third_res)

        if third_res[0] == "Correct!":
            break
        sock.close()

        #time.sleep(1.0)

        i = i + 0.01
        j = j + 0.01
