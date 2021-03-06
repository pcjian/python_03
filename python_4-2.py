department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 2445566.1234
COURSE_FEES_Python = 12333.5676

#line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End'%(department1,depart1_m,COURSE_FEES_SEC)
#line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End'%(department2,depart2_m,COURSE_FEES_Python)


line1 = f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FEES:{COURSE_FEES_SEC:<10.2f}'
line2 = f'Department2 name:{department2:<10} Manager:{depart2_m:<10} COURSE FEES:{COURSE_FEES_Python:<10.2f}'


length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)