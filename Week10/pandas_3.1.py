import pandas as pd

df = pd.read_csv("./Week10/auto-mpg.csv", header=None)
df_columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())    # 처음 5개 행
print('\n')
print(df.tail())    # 마지막 5개 행

print(df.shape)     # 데이터 프레임의 크기
print(df.info())    # df의 내용 확인
print(df.describe())    # df의 기술 통계 정보 확인
print('\n')
print(df.describe(include='all'))
print(df.dtypes)