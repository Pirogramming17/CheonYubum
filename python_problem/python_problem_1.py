num = 0

while True:
    try:
        x = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
    except:
        print('정수를 입력하세요')
    else:
        if x < 1 or x > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            break

for i in range(x):
    num += 1
    print('Player : ', num)