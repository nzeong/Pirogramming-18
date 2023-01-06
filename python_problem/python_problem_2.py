dict_st = {}


#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, mid_score, final_score) :
    dict_st[name] = dict(mid=mid_score, final=final_score)


##############  menu 2
def Menu2(name) :

    mean = int((dict_st[name]["mid"]+dict_st[name]["final"])/2)

    if mean >= 90:
        dict_st[name]['grade']='A'
    elif mean >= 80:
        dict_st[name]['grade']='B'
    elif mean >= 70:
        dict_st[name]['grade']='C'
    else:
        dict_st[name]['grade']='D'
    
    #학점 부여 하는 코딩

##############  menu 3
def Menu3() :
    print('''
---------------------------
name   mid   final   grade
---------------------------''')

    for name in dict_st:
        print(f'{name}    {dict_st[name]["mid"]}     {dict_st[name]["final"]}      {dict_st[name]["grade"]}')
    

##############  menu 4
def Menu4(del_name):

    del dict_st[del_name]
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
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

        student_information = input('Enter name mid-score final-score : ').split()

        try:
            if len(student_information) != 3:
                raise Exception("Num of data is not 3!")
                
            name = student_information[0]
            mid = student_information[1]
            final = student_information[2]

            if name in dict_st:
                raise Exception("Already exist name!")

            if not(mid.isdigit()):
                raise Exception("Score is not positive integer!")
            if not(final.isdigit()):
                raise Exception("Score is not positive integer!")

            Menu1(name, int(mid), int(final))
        except Exception as e:
            print(e)
        
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :


        try:
            if not dict_st:
                raise Exception("No student data!")
                                
            print("Grading to all students.")

        except Exception as e:
            print(e)

        else:
            for name in dict_st:
                if len(dict_st[name]) != 3:
                    Menu2(name)
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        try:
            if not dict_st:
                raise Exception("No student data!")
            for i in range(len(dict_st)):
                if len(dict_st[name]) != 3:
                    raise Exception("There is a student who didn't get grade.")
            Menu3()

        except Exception as e:
            print(e)
        
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :

        try:
            if not dict_st:
                raise Exception("No student data!")

            del_name = input("Enter the name to delete : ")
            if del_name not in dict_st:
                                raise Exception("Not exist name!")

            Menu4(del_name)
            print("{0} student information is deleted.".format(del_name))

        except Exception as e:
            print(e)        
        
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!")
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.")
        #"Wrong number. Choose again." 출력
