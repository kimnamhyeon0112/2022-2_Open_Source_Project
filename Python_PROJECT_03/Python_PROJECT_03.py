# Unit 12
my_hero_key = input().split()
my_hero_value = input().split()

key_with_value = dict(zip(my_hero_key, my_hero_value))
print(key_with_value)

# Unit 13
cost = int(input())
coupon = str(input())
if coupon == 'Cash3000':
    cost -= 3000
elif coupon == 'Cash5000':
    cost -= 5000
print(cost)

# Unit 14
kor, eng, math, sci = map(int, input().split())
average = (kor + eng + math + sci) / 4
if  0 > kor or 100 < kor or 0 > eng or 100 < eng or 0 > math or 100 < math or 0 > sci or 100 < sci:
    print('잘못된 점수')
else:
    if average >= 80:
        print('합격')
    else:
        print('불합격')
        
# Unit 15
age = int(input())
balance = 9000
if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif 19 <= age:
    balance -= 1250
print(balance)