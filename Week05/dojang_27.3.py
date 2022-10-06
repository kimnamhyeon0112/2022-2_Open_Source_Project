import pickle           # pickle 모듈 사용

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
with open('james.p','wb') as file:  # binary 파일로 씀
    pickle.dump(name, file)         # pickle 모듈의 dump 메소드를 사용하여 name을 james.p에 씀
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
    
import pickle
with open('james.p','rb') as file:  # binary 파일을 읽음
    name = pickle.load(file)        # 파일에 있는 name을 읽어옴
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)