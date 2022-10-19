class Counter:
    def __init__(self, stop):
        self.stop = stop
        
    def __getitem__(self, index):           # __getitem__으로 인덱스 받음
        if index < self.stop:
            return index
        else:
            raise IndexError                # 범위의 오류로 인한 인덱스 초과 에러
        
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
for i in Counter(3):
    print(i, end=' ')