#1000 이하의 소수가 들어있는 리스트
#에라토스테네스의 체를 활용할 수 있지만 그냥 무식하게 구함.
#매번 소수임을 판정하면 비효율적이니, 미리 1000까지의 소수를 구해두고 시작.

prime_number = [2]

for i in range(2,1000):
    for j in range(len(prime_number)):
        if i % prime_number[j] == 0:
            break
    else:
        prime_number.append(i)

prime_number_set = set(prime_number) # 시간 복잡도를 줄이기 위해 set에 저장
# 시간 복잡도가 궁금하면 나중에 물어보고

#소수를 구할때마다 집어넣고, 다음번 구할 때 지금까지 구한 소수로 모두 나눠보는 방식
#for ~ else 구문: for문에 있는 것을 모두 수행하고, break가 되지 않았다면 else구문 수행

#1
length = 0
n = 1
answer_1 = []
while length < 5: #5 개가 될 때까지 반복
    if n**2-2 in prime_number_set :
        answer_1.append(n**2-2) #n의 2제곱-2가 소수일 경우,
        # answer_1 이라는 리스트에 추가
        length += 1 # length에 1 추가
    n += 1
print('answer1',answer_1)

#2
answer_2 = []
for i in range(10):
    answer_2.append((prime_number[i+10]**2 - prime_number[i+9])%24) #나머지 구하기
    #시험삼아 몇개 해봤지만 안 나눠짐
print('answer2, 대충 10개만 구해봄',answer_2)

#3
answer_3 = []
count = 0
for elements in prime_number:
    if (elements + 50) in prime_number_set:
        answer_3.append(elements+50)
    if len(answer_3) == 5:
        break
print('answer3',answer_3)