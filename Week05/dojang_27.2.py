with open('hello.txt','w') as file:
    for i in range(3):
        file.write('Hello world {0}\n'.format(i))       # hello world뒤에 0부터 i까지 숫자를 출력
        
lines = ['안녕하세요\n', '파이썬\n', '코딩도장입니다\n']
with open('hello.txt','w') as file:
    file.writelines(lines)        # writelines: 리스트에 들어있는 문자열을 파일에 씀, 또한 각 문자열 끝에 \n을 붙이면 \n단위로 한줄씩 들여씀
    
with open('hello.txt','r') as file:
    lines = file.read()           # 파일의 내용을 파일에 입력된 내용대로 읽어와서
    print(lines)                  # 터미널에 출력
    
with open('hello.txt','r') as file:
    lines = None                    # None으로 초기화하지 않고 한줄씩 읽으려하면 Error
    while lines != '':
        lines = file.readline()     # readline: 파일의 내용을 한줄씩 읽음
        print(lines.strip('\n'))    # strip: 파일에서 \n은 삭제하고 출력, strip을 안쓰면 \n도 같이 읽어 한줄 띄고 내용 출력
        
with open('hello.txt','r') as file:
    for line in file:
        print(line.strip('\n'))     # 위의 코드의 for문을 사용한 축약버전