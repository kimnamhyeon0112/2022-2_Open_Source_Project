def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)          # *을 두번 사용하는 이유는 딕셔너리의 키와 값을 매핑해줘야 하기 때문 따라서 *을 한번만 쓰면 키만 출력

def personal_info(**kwargs):            # 키워드 인수 kwargs를 사용
     for kw, arg in kwargs.items():
         print(kw, ': ', arg, sep='')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')