import csv
import os
print("\n\n\n\n")
path = 'word_table.txt'
f = open(path,'rt',encoding='UTF8')
line = f.readlines()
eng_words= str(line[0]).split(',')
kor_words = str(line[1]).split(',')
'''
print(eng_words)
print(kor_words)
'''

def get_int_and(s):
    print()
    p = False
    u = 0
    while True :
        u = input(s)
        try :
            u = int(u)
            p = True
            break
        except :
            print("다시 입력해주세요.")
            continue
    if p :
        return u



print("Hello world!")
res = check_right('      ...에 따르면      '.strip(),2,0)
print("res : ",res)


