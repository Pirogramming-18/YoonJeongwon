# 학생들 정보 저장 dictionary {'st1': [90, 90, A], 'st2': [80, 90, B] }
students_info = dict()

##############  menu 1
def Menu1() :
  global students_info
  stu_info = input('Enter name mid-score final-score :').split()

  if len(stu_info) != 3:
    print('Num of data is not 3')
  elif stu_info[0] in students_info:
    print('Already exist name!')
  else:
    for i in range(1,3):
      if stu_info[i].isdigit() and int(stu_info[i]) >= 0 :
        pass
      else:
        print('Score is not positive integer!')
        return
    students_info[stu_info[0]] = [int(stu_info[1]), int(stu_info[2])]
  #사전에 학생 정보 저장하는 코딩 

##############  menu 2
def Menu2() :
  if students_info:
    for i in students_info:
      if len(students_info[i]) == 2:
        avg = (students_info[i][0] + students_info[i][1])/2
        grade = 'D'
        if avg >= 90:
          grade = 'A'
        elif avg >= 80:
          grade = 'B'
        elif avg >= 70:
          grade = 'C'
        students_info[i].append(grade)
      else:
        print('Grading to all students.')
  else:
    print('No student data!')
  #학점 부여 하는 코딩

##############  menu 3
def Menu3() :
  if students_info:
    print('----------------------------------------')
    print('name\t\tmid\tfinal\tgrade')
    print('----------------------------------------')  
    for i in students_info:
      if len(students_info[i]) == 3:
        print('{:<16}{:<9}{:<9}{:<9}'.format(i,students_info[i][0],students_info[i][1],students_info[i][2]))
      elif len(students_info[i]) == 2:
        print('{:<16}{:<9}{:<9}'.format(i,students_info[i][0],students_info[i][1]))
  else:
    print('No student data!')
  #출력 코딩

##############  menu 4
def Menu4():
  if students_info:
    stu_name = input('Enter the name to delete :')
    if stu_name in students_info:
      try:
        del students_info[stu_name]
      except KeyError as e:
        print(e)
      else:
        print(stu_name, 'student information is deleted.')
    else:
      print('Not exist name!')
  else:
    print('No student data!')
  #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
def program():
  print("*Menu*******************************")
  print("1. Inserting students Info(name score1 score2)")
  print("2. Grading")
  print("3. Printing students Info")
  print("4. Deleting students Info")
  print("5. Exit program")
  print("*************************************")
  while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
      Menu1()
      #학생 정보 입력받기
      #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
      #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2":
      Menu2()
      #예외사항 처리(저장된 학생 정보의 유무)
      #예외사항이 아닌 경우 2번 함수 호출
      #"Grading to all students." 출력

    elif choice == "3":
      Menu3()
      #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
      #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4":
      Menu4()
      #예외사항 처리(저장된 학생 정보의 유무)
      #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
      #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
      #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5":
      print("Exit Program!")
      break
      #프로그램 종료 메세지 출력
      #반복문 종료

    else :
      print("Wrong number. Choose again.")
      #"Wrong number. Choose again." 출력

program()