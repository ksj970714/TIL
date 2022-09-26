X = input()
X += '+'

value = 0
temp = ''
switch = 0
for word in X:

    if word == '+' and switch == 0:
        value += int(temp)
        temp = ''
    elif word == '+' and switch == 1:
        value -= int(temp)
        temp = ''
    elif word == '-' and switch == 0:
        switch = 1
        value += int(temp)
        temp = ''
    elif word == '-' and switch == 1:
        value -= int(temp)
        temp = ''
    else:
        temp += word

print(value)

# 단적으로 마이너스 뒤에 오는 것은 전부 -다. 라고 생각해도 무방하다.
# 맨처음 만날때까진 더하기, 그다음 만날때부터 계산

