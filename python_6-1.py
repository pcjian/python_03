import re
str1 = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO'

str2 = 'TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'

l1 = re.match('TCP Student\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+Teacher\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\,\s+.*,\s+bytes\s*(\d+),\s+flags\s+(\w+)',str1).groups()

l2 = re.match('TCP Student\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+Teacher\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\,\s+.*,\s+bytes\s*(\d+),\s+flags\s+(\w+)',str2).groups()

# t11 = (l1[0],l1[1],l1[2],l1[3])
# t12 = (l1[4],l1[5])
#
# t21 = (l2[0],l2[1],l2[2],l2[3])
# t22 = (l2[4],l2[5])
#
# d = {}
# d[t11] = t12
# d[t21] = t22

l11 = l1[0:4],l1[4:]
l21 = l2[0:4],l2[4:]

d = {}
d[l11[0]] = l11[1]
d[l21[0]] = l21[1]
print('打印字典')
print(d)
print('格式化打印输出')
for key,value in d.items():
    #print(key[0],key[1],key[2],key[3],value[0],value[1])
    print('%10s : %-20s|%10s : %-20s|%10s : %-20s|%10s : %-20s|\n%10s : %-20s|%10s : %-20s|' % ('src',key[0],'src_p',key[1],'dst',key[2],'dst_p',key[3],'bytes',value[0],'flags',value[1]))
    print('='*140)
