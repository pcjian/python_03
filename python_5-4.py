import re
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/1/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
result = sorted(port_list,key=lambda x:(int(re.match('^eth(\d)/(\d{3})/(\d)/(\d{1,2})',x).groups()[2]),int(re.match('^eth(\d)/(\d{3})/(\d)/(\d{1,2})',x).groups()[3]))

print(result)