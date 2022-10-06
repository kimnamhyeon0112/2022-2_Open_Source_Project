file = open('hello.txt', 'w')       # hello.txt를 쓰기모드로 실행
file.write('Hello world')           # hello.txt에 Hello world 입력
file.close()                        # 파일 닫기
print()

file = open('hello.txt','r')        # hello.txt를 읽기모드로 실행
s = file.read()                     # s라는 변수에 hello.txt 파일의 내용을 터미널로 출력하게끔 저장
print(s)
file.close()
print()

with open('hello.txt','r') as file:     # 이 구문을 사용하면 file을 자동으로 닫아주므로 file.close()를 할 필요가 없음
    s = file.read()
    print(s)