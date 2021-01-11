# 수강생 관리 시스템
students=[]
id = 1

while True :
    print("===== cloud 반 수강생 관리 시스템 =====")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")
    menu = input("메뉴를 선택하세요")
    if menu == "1" :
        name = input("이름 : ")
        age = input("나이 : ")
        while not age.isdecimal() :
            print("나이는 숫자로 입력해 주세요.")
            age = input("나이 : ")
        major = input("전공 : ")

        student = {"id":id, "name":name, "age":int(age), "major":major}
        students.append(student)
        print("{0}(이)가 등록 되있습니다.".format(name))
        id += 1
    elif menu == "2" :
        print("===== 수강생 목록 보기 =====")
        print(students)
    elif menu == "3" :
        id = input("수정 할 수강생 번호 : ")
        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요.")
            id = input("수정 할 수강생 번호 : ")
        major = input("수정 할 전공 : ")
        for students in students :
            if student["id"] == int(id) :
                student["major"] = major
                print("{0}의 정보가 수정되었습니다.".format(student["name"]))
                break
        
    elif menu == "4" :
        id = input("삭제 할  수강생 번호 : ")
        while not id.isdecimal() :
            print("수강생 번호는 숫자로 입력해 주세요.")
            id = input("삭제 할 수강생 번호 : ")
        for student in students :
            if student["id"] == id :
                delete = input(("{0}의 정보를 삭제하시겠습니까.? [y/n]".format(student["name"])))
                if delete == 'y' or delete == 'Y' :
                    students.remove(student)
                    print("{0}의 정보가 삭제 되었습니다.",format(student[id]))
                    break
    elif menu == "0" :
        print("수강생 관리 프로그램을 종료합니다.")
        break
    else :
        print()
        print("1,2,3,4,0 번 중 선택하세요.")
