import os
import re
ifconfig_result = os.popen('ifconfig ens33').read()
re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)
# for ip in re_findall_result:
#     if ip[0:3] == '255' :
#         mask = ip
#     elif ip[-3:] == '255' :
#         broadcast = ip
#     else:
#         ipv4_ip = ip
for ip in re_findall_result:
    if re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',ip).groups()[0] == '255' :
        mask = ip
    elif re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',ip).groups()[3] == '255' :
        broadcast = ip
    else:
        ipv4_ip = ip

print('%20s : %-20s'%('Network Mask',mask))
print('%20s : %-20s'%('Broadcast',broadcast))
print('%20s : %-20s'%('Ipv4 Addr',ipv4_ip))



