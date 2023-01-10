#첫 번째 파이썬 명령어
print(2 + 3)
print(2 ** 3)

#문자열(String)
print("Ola")
print("Hi there " + "Ola")
print("Ola"*3)
print("Runnin' down the hill")
print('Runnin\' down the hill')
print("Ola".upper())
print(len("Ola"))

#오류
# print(len(304023))
print(len(str(304023)))

#변수
name = "Ola"
print(name)
name = "Sonja"
print(name)
print(len(name))
a = 4
b = 6
print(a * b)

#print() 함수
name = 'Maria'
print(name)

#리스트(List)
print([])
lottery = [3,42,12,19,30,59]
print(len(lottery))
lottery.sort()
print(lottery)
lottery.reverse()
print(lottery)
lottery.append(199)
print(lottery)
print(lottery[0])
print(lottery[1])
print(lottery)
lottery.pop(0)
print(lottery)

#딕셔너리(Dictionary)
print({})
participant = {'name':'Ola', 'country':'Poland', 'favorite_numbers':[7, 42, 92]}
print(participant['name'])
participant['favorite_language'] = 'Python'
print(len(participant))
participant.pop('favorite_numbers')
print(participant)
participant['country'] = 'Germany'
print(participant)

#비교하기
print(5>2)
print(3<1)
print(5>2*2)
print(1==1)
print(5!=2)
print(6>=12/2)
print(3<=2)
print(6>2 and 2<3)
print(3>2 and 2<1)
print(3>2 or 2<1)

#Boolean(불리언)
a = True
print(a)
a = 2>5
print(a)