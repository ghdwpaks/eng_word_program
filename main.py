import csv
import os
print("\n\n\n\n")
'''
print(eng_words)
print(kor_words)
'''

def get_int(s):
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



def check_right(userans,  pronum ,words,show_ans=0) :
    #show_ans 가 1 이면 바로 보여주고 0이면 안보여주기
    '''
    print("userans:{}".format(userans))
    print("pronum:{}".format(pronum))
    print("eng_or_kor:{}".format(eng_or_kor))
    '''
    #print("userans :{}".format(userans))
    userans = (userans).strip().split(" ")
    ps = False#맞으면 true, 틀리면 False
    right_ans_count = 0
    right_ans = (words[pronum]).strip().split(" ")
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
            #print("오류가 발생했습니다.")
            break
    if right_ans_count >= len(right_ans) and len(userans) == len(right_ans) :
        ps = True
        if show_ans == 1 :
            print("맞았습니다!")
    else :
        if show_ans == 1 :
            print("정답은 {}입니다.".format(words[pronum].strip()))
        ps = False
    return ps

def test_words(path,eng_or_kor,show_ans=0) :
    wrong_ans = []
    correct_count = 0
    f = open(path,'rt',encoding='UTF8')
    line = f.readlines()
    eng_words= str(line[0]).split(',')
    kor_words = str(line[1]).split(',')
    right_words = []
    show_words = []
    if eng_or_kor == 1 : #답이 한글
        right_words = kor_words #이 시점에서 right_words는 문자열 상태이다
        show_words = eng_words
        #단어'들'이 들어있는것은 kor_words가 된다.
    elif eng_or_kor == 0 : #답이 영어
        right_words = eng_words
        show_words = kor_words

    for i in range(0,len(right_words)) :
        userans_word = input("{}\n>>".format(show_words[i]))
        if check_right(userans_word,i,right_words,show_ans) :
            correct_count += 1
        else :
            wrong_ans.append(i)
    print("맞은 갯수는 {}개 입니다!".format(correct_count))
    print("틀린문제는",end="")
    if len(wrong_ans) <= 0 :
        print(" 없습니다.")
    else :
        print()
        for i in range(0,len(wrong_ans)) :
            print("{}번의 '{}'".format(wrong_ans[i]+1,right_words[wrong_ans[i]].strip()))
        print("들이 있습니다.")

    
        





print("Hello world!")
while True :
    
    path = ''
    print("현재 시험 가능 과목은 1과 입니다.")
    userans_check_unit = get_int("몇과를 시험볼건지 정해주세요. >>")

    userans_check_language = get_int("영어를 입력할거면 0, 한글을 입력할거면 1. >>")
    show_ans = get_int("틀린 답을 바로 공개할거면 1, 아니면 0. >>")
    if userans_check_language == 1 or userans_check_language == 0 :
        if userans_check_unit == 1 :
            path = './words_file/word_table1.txt'
            test_words(path,userans_check_language,show_ans)
        else :
            continue
    else :
        continue

    




