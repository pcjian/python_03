import os
import re

route_result = os.popen('route -n').read()

re_result = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)',route_result)

len = len(re_result)

for x in [0,len-1]:
    if re_result[x][3] == 'UG':
        print('网关为：%s'%(re_result[x][1]))
