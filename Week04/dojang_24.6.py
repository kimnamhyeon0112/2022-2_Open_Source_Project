a = list(map(int,input().split(';')))
a.sort(reverse=True)
for price in a:
    print('{:>9,}'.format(price))