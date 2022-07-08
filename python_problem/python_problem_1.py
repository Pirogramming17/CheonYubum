import random
num = 0

def brGame():
  while True:
    try:
      x = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
    except:
      print('정수를 입력하세요')
    else:
      if x < 1 or x > 3:
        print('1,2,3 중 하나를 입력하세요')
      else:
        break

      return x


while True:
    x = random.randint(1, 3)
    for i in range(x):
        num += 1
        print('Computer : ', num)
        if num >=31:
            print('Player win!')
            break
    
    x = brGame()
    for i in range(x):
        num += 1
        print('Player : ', num)
        if num >=31:
            print('Computer win!')
            break