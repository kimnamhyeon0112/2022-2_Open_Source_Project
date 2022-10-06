def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)
personal_info('홍길동', 30, '서울시 용산구 이촌동')                         # 함수에 들어가는 인자를 순서대로 출력
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')        # 함수의 인자와 키워드를 매칭
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')        # 키워드를 사용하면 순서를 지키지 않아도 알아서 맞춤