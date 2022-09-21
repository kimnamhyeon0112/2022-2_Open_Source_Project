if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')
print()

if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')
print()

if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓
print()

if not 0:
    print('참')    # not 0은 참
 
if not None:
    print('참')    # None은 참
 
if not '':
    print('참')    # not 빈 문자열은 참
print()