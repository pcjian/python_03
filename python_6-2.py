import os

os.mkdir('test1')
os.chdir('test1')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.write('this is the second qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

l = os.listdir(os.getcwd())

ll = []

for c in l:
    if os.path.isfile(c):
        for line in open(c):
            if 'qytang' in line:
                if not c in ll:
                    ll.append(c)

print('文件中包含"qytang"关键字的文件为：')

for x in ll:
    print('\t',end='')
    print(x)





