a = {i for i in 'apple'}        # set의 요소는 중복될수 없으므로
print(a)                        # 결과는 a,p,l,e 단, set의 요소는 순서상관 없으므로 결과는 항상 순서가 바뀜
print()

a = {i for i in 'pineapple' if i not in 'apl'}      # pineapple에서 a,p,l을 모두 생략하고 요소 출력
print(a)                                            # 결과는 i,e,n 출력