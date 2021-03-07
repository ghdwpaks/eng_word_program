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

def ans_split(s) :
    if '에' in s :
        return '에'
    elif '을' in s :
        return '을'
    elif '에서' in s :
        return '에서'
    elif '할' in s :
        return '할'
    else :
        return s



def check_right(userans,pronum,eng_or_kor) :
    '''
    print("userans:{}".format(userans))
    print("pronum:{}".format(pronum))
    print("eng_or_kor:{}".format(eng_or_kor))
    '''
    #print("userans :{}".format(userans))
    userans = userans.split(" ")
    ps = False#맞으면 true, 틀리면 False
    right_ans_count = 0
    if eng_or_kor == 0 : #답이 한글
        right_ans = (kor_words[pronum]).strip().split(" ")
    elif eng_or_kor == 1 : #답이 영어
        right_ans = (eng_words[pronum]).strip().split(" ")
    '''
    print('right_ans:{}'.format(right_ans))
    print("len(right_ans):{}".format(len(right_ans)))
    print("right_ans.count(' '):{}".format(right_ans.count(" ")))
    print("right_ans_count:{}".format(right_ans_count))
    '''
    for i in range(0,len(right_ans)) :
        #print("i :",i)
        try :
            #print(1)
            if i == 0 :
                #print(2)
                '''
                print("userans[{}]:{}".format(i,userans[i]))
                print("right_ans[{}]:{}".format(i,right_ans[i]))
                '''
                userans[i] = ans_split(userans[i])
                #print(3)
                right_ans[i] = ans_split(right_ans[i])
                '''
                print("userans[{}] :{}".format(i,userans[i]))
                print("right_ans[{}] :{}".format(i,right_ans[i]))
                '''
            #print("right_ans_count:{}".format(right_ans_count)) 
            #print("userans[i] == right_ans[i]",userans[i] == right_ans[i])   
            if userans[i] == right_ans[i] :
                
                right_ans_count += 1
                #print("right_ans_count:{}".format(right_ans_count))
        except :
            ps = False
            print("오류가 발생했습니다.")
            break
    if right_ans_count >= len(right_ans) and len(userans) == len(right_ans) :
        ps = True
    else :
        ps = False
    return ps



print("Hello world!")
res = check_right('      ...에 따르면      '.strip(),2,0)
print("res : ",res)


