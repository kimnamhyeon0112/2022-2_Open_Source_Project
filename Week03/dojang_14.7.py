kor, eng, math, sci = map(int, input().split())
average = (kor + eng + math + sci) / 4
if  0 > kor or 100 < kor or 0 > eng or 100 < eng or 0 > math or 100 < math or 0 > sci or 100 < sci:
    print('잘못된 점수')
else:
    if average >= 80:
        print('합격')
    else:
        print('불합격')