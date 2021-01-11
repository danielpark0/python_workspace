# dictionary type : variable_name = {"name":"value",...} value : int, float, boolean, str, list
# {"name":"value",...} value : int, float, boolean, str, list
student = {"name" : "daniel", "age" : 3, "major" : "computer"}
students = []
students[0] = student

for s in students:
    print("이름 : {0} 나이 : {0} 전공 : {0}".format(student["name"], student["age"], student["major"]))

# dictionary 추가 수정 : "name" : value 쌍으로 추가 수정 ("name" 존재하면 수정, 존재하지 않으면 추가)
students[0]["studentid"] = "Cloud"
print(students[0])
students[0]["major"] = "art"
print(students[0])

# dictionary 삭제
del students[0]["studentid"]
print(students[0])

#get() : key check 없는 경우 None return
key_value = input("student 속성 입력 (name, age, major)")
if student[0].get(key_value) == None :
    key_value = input("student 속성 입력 (name, age, major)")
print("{0} key의 value 값 : {1}".format(key_value, students[0][key_value]))