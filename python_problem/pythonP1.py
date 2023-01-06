num = 0

input_num = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

while True:
  if input_num.isdigit():
    if input_num == '1':
      break
    elif input_num == '2':
      break
    elif input_num == '3':
      break
    else:
      input_num = input('1,2,3 중 하나를 입력하세요')
  else:
    input_num = input('정수를 입력하세요')
