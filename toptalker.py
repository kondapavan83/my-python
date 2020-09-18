#####
#Top Talker Connections on ASA
#####
#Author:
#Naga Konda
#####
#import paramiko
import re
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('sc-fw-01.net.op3n-tabe.com',port=22,username='abc',password='xxx')
# stdin,stdout,stderr=ssh.exec_command('show  conn')
# a=stdout.readlines()
f=open("/Users/abc/Desktop/connections1.txt","r")
a=f.readlines()
f.close()
#ssh.close()
b=[]
c={}
for i in a:
  if re.match("TCP\s+\w+\s+(\d+\.\d+\.\d+\.\d+)\:\d+.*",i):
    b.append(re.match("TCP\s+\w+\s+(\d+\.\d+\.\d+\.\d+)\:\d+.*",i).groups()[0])

for i in set(b):
  c[i]=b.count(i)

c=sorted(c.items(),key=lambda c:c[1],reverse=True)
print(c[:10])
