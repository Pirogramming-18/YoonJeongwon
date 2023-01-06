num = 0

def print_play(input_num, name):
  global num
  for i in range(int(input_num)):
    num += 1
    print(name, ':', num)
    if(num == 31):
      break

def speak_num(name):
  input_num = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')

  while True:
    if input_num.isdigit():
      if input_num == '1':
        print_play(input_num, name)
        break
      elif input_num == '2':
        print_play(input_num, name)
        break
      elif input_num == '3':
        print_play(input_num, name)
        break
      else:
        input_num = input('1,2,3 중 하나를 입력하세요')
    else:
      input_num = input('정수를 입력하세요')

def brGame(name1, name2):
  while True:
    speak_num(name1)
    if num == 31:
      print(name2, 'win!')
      break
    speak_num(name2)
    if num == 31:
      print(name1, 'win!')
      break

brGame('playerA', 'playerB')
