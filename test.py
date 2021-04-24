s = "portray,markedly,contemporary,mainstream,blindfold,harsh,criticism,admire,illustrated,botanical,observe,exotic,hothouse,coexist,naive,surrealism,pursue"
s = s.split(",")
for i in s :
    print("{} :".format(i))











s = """묘사:
현저하게:
동시대의:
주류:
눈가리개:
가혹한:
비판:
감탄하다:
그림:
식물:
다음을 준수하다.
이국적:
하우스:
공존:
순진함:
초현실주의:
다음을 추구한다:
"""
s = s.split(":\n")
for c in s:
    print(c,end=",")
