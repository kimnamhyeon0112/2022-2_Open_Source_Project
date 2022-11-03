# -*- coding: utf-8 -*-

# pandas 불러오기
import pandas as pd

# key:value 쌍으로 딕셔너리를 만들고 변수 dict_data에 저장
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}

# Series()함수로 딕셔너리를 Series로 변환하여 sr에 저장
sr = pd.Series(dict_data)

print(type(sr))
print('\n')
print(sr)