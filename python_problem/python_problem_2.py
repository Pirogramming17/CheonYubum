##############  menu 1
def Menu1(student, user) :
    #사전에 학생 정보 저장하는 코딩
    student[user[0]] = [int(user[1]), int(user[2])]   

##############  menu 2
def Menu2(student) :
    #학점 부여 하는 코딩
    for key in student :
        if len(student[key]) != 3 :
            avg_score = (student[key][0]+student[key][1])/2
            if avg_score >= 90 :
                student[key].append('A')
            elif avg_score >= 80 :
                student[key].append('B')
            elif avg_score >= 70 :
                student[key].append('C')
            else:
                student[key].append('D')
        
##############  menu 3
def Menu3(student) :
    print()
    print('---------------------------')
    print('{:<7}{:>5}{:>7}{:>7}'.format('name','mid','final','grade'))
    print('---------------------------')
    for key in student:
        print('{:<7}{:>5}{:>7}{:>7}'.format(key, student[key][0], student[key][1], student[key][2]))

##############  menu 4
def Menu4(student, name) :
    #학생 정보 삭제하는 코딩
    del student[name]

def gradingCheck(student):
    for key in student:
            if len(student[key]) != 3:
                return 1

student = {}

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        user = input("Enter the student's name, mid-score, final-score : ").split(' ')
        if len(user) != 3 :
            print('Input data is not 3')
        elif user[0] in student:
            print('Already exist data')
        elif not user[1].isdigit() or not user[2].isdigit():
            print('Score is not positive integer')
        elif int(float(user[1])) != float(user[1]) or int(float(user[2])) != float(user[2]) or int(user[1])<0 or int(user[2])<0:
            print('Score is not positive integer')
        else :
            Menu1(student, user)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if not student: 
           print('No related data')
        else :
            Menu2(student)
            print('Grading to all students.')

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        gradingFlag = 1
        if not student: 
           print('No related data')
        else :
            if gradingCheck(student) :
                print("Student who didn't get grade exists.")
            else :
                Menu3(student)               
        
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if not student: 
           print('No related data')
        else :
            name = input('Enter the name to delete : ')
            if not name in student:
                print('Not exist name!')
            else :
                Menu4(student, name)
                print('%s student information is deleted.'%name)

    elif choice == "5":
        #프로그램 종료 메세지 출력
        #반복문 종료
        print('프로그램 종료')
        break

    else :
        #"Wrong number. Choose again." 출력
        print('Wrong number. Choose again.')