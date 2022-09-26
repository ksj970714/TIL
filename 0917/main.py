words = input()
boom = input()

stack = ''
stacklength = []
switch = 0
newword = ''
length = len(boom)

token = 0

for word in words:
    print(stack ,'new',newword, stacklength,token,word)

    if word == boom[0] and switch == 0:
        switch = 1
        stacklength.append(0)
        # 순서대로 안 들어오면 반환할 스택

    if switch == 1:
        token = 1
        if stacklength[-1] < length:  # 원래 들어오는 것에 삽입

            if boom[stacklength[-1]] == word:
                stack += word
                stacklength[-1] += 1

            elif boom[0] == word:
                stacklength.append(1)
                stack += word
            else:
                stack += word
                stacklength = []
                switch = 0
                newword += stack
                stack = ''
                token = 0
                continue

            if stacklength[-1] == length:

                if stack[-length:] == boom:
                    stack = stack.replace(boom, '')

                    stacklength.pop()
                if stack == '':
                    switch = 0

    if switch == 0 and token == 0:
        newword += word

    token = 0
newword += stack
if newword == '':
    newword = 'FRULA'

print(newword)