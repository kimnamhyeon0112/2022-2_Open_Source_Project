x = 10
y = 3

def get_quotient_remainder(a,b):
    return a//b, a%b                # //: 정수형, /: 실수형

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))