with open("words2.txt","r") as file:
    word = None
    while word != '':
        word = file.readline().strip('\n')
        if word == word[::-1]:
            print(word)