import os
import re
ifconfig_result = os.popen('ifconfig ens33').read()

re_findall_result = re.findall('[0-9a-f]{0,2}\:[0-9a-f]{0,2}\:[0-9a-f]{0,2}\:[0-9a-f]{0,2}\:[0-9a-f]{0,2}\:[0-9a-f]{0,2}',ifconfig_result)

print('MAC地址为：%s'%(re_findall_result[0]))