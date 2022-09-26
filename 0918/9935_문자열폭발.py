oldword = input()
boom = input()

stack = []
newword = ''
stack_len = []
boom_len = len(boom)
switch = 0

for word in oldword:
    if word == boom[0]:
        switch = 1
        stack_len.append(0)

    if switch == 1:
        if boom[stack_len[-1]] == word:
            stack.append(word)
            stack_len[-1] += 1

        else:
            stack.append(word)

            newword += ''.join(stack)
            stack = []
            stack_len = []
            switch = 0
            continue

        if stack_len[-1] == boom_len:
            for i in range(boom_len):
                stack.pop()
            stack_len.pop()
            if stack == []:
                switch = 0

    else:
        newword += word

newword += ''.join(stack)
if newword == '':
    print('FRULA')
else:
    print(newword)


'''
배운 점
문자열의 replace 메서드가
생각보다 시간 복잡도가 크다.
리스트가 스택으로 구현할때 생각보다 장점이 많다..!
'''