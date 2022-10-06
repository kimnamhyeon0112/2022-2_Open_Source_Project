word = input('단어를 입력하세요: ')
is_palindrome = True                # 회문을 판별할 변수로 초기값은 True
for i in range(len(word)//2):       # 문자열 길이의 절반만큼 loop
    if word[i] != word[-1-i]:       # word[i]와 word[-1-i]의 길이가 다르면  
        is_palindrome = False       # 회문이 아니므로 false
        break
    
print(is_palindrome)
print()

word = input('단어를 입력하세요: ')
print(word == word[::-1])           # 슬라이스를 이용하여 원래 문자와 뒤집은 문자 비교
print()

word = 'level'
print(list(word) == list(reversed(word)))   # string을 리스트로 만들고, 그 리스트를 뒤집어 비교
print(word == ''.join(reversed(word)))