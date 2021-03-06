import re

str1 = 'Port-channel1.189    192.168.189.254   YES   CONFIG   up'

result1 = re.match('(\w+\-\w+\d+\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)',str1).groups()

line11 = '%-20s :%-20s'%('接口',result1[0])
line12 = '%-20s :%-20s'%('IP地址',result1[1])
line13 = '%-20s :%-20s'%('状态',result1[4])
str21 = '接口'
str22 = 'IP地址'
str23 = '状态'
line21 = f'{str21:<20} :{result1[0]:<20}'
line22 = f'{str22:<20} :{result1[1]:<20}'
line23 = f'{str23:<20} :{result1[4]:<20}'

str31 = 'VLAN ID'
str32 = 'MAC'
str33 = 'Type'
str34 = 'Interface'

str2 = '166 54a2.74f7.0236   DYNAMIC Gi1/0/11'

result2 = re.match('(\d{1,4})\s+([a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+(\w+)\s+(\w+\d\/\d\/\d{1,2})',str2).groups()

line31 = '%-20s :%-20s'%(str31,result2[0])
line32 = '%-20s :%-20s'%(str32,result2[1])
line33 = '%-20s :%-20s'%(str33,result2[2])
line34 = '%-20s :%-20s'%(str34,result2[3])

line41 = f'{str31:<20} :{result2[0]}'
line42 = f'{str32:<20} :{result2[1]}'
line43 = f'{str33:<20} :{result2[2]}'
line44 = f'{str34:<20} :{result2[3]}'

print('-'*100)
print(line11)
print(line12)
print(line13)
print('-'*100)
print(line21)
print(line22)
print(line23)
print('-'*100)
print(line31)
print(line32)
print(line33)
print(line34)
print('-'*100)
print(line41)
print(line42)
print(line43)
print(line44)
