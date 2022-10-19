class Counter:
    def __init__(self, stop):
        self.current = 0            # 현재 숫자 유지, 0 ~ stop
        self.stop = stop            # 반복을 끝낼 숫자
        
    def __iter__(self):
        return self                 # 현재 인스턴스(self)반환
    
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 마지막 숫자보다 작으면
            r = self.current            # 현재 숫자를 r에 저장
            self.current += 1           # r + 1
            return r
        else:                           # current >= stop
            raise StopIteration         # 예외처리후 종료
        
for i in Counter(3):
    print(i, end=' ')
print()

a, b, c = Counter(3)
print(a,b,c)
a, b, c, d, e = Counter(5)
print(a, b, c, d, e)