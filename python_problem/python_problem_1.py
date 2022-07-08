num = 0
time = 0
turn = 0

while True:
    time += 1
    try:
        x = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
    except:
        print('정수를 입력하세요')
    else:
        if x < 1 or x > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            for i in range(x):
              num += 1
              if time % 2 != 0:
                print('PlayerA : ', num)
                turn = 1
                if num == 31:
                  print('PlayerB win!')
                  break
              else:
                print('PlayerB : ', num)
                turn = 2
                if num == 31:
                  print('PlayerA win!')
                  break