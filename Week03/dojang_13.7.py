cost = int(input())
coupon = str(input())
if coupon == 'Cash3000':
    cost -= 3000
elif coupon == 'Cash5000':
    cost -= 5000
print(cost)