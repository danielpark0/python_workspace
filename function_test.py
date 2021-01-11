# def 함수명 ([argumentlist]) :
#     구현
#     [return data]
# 함수는 정의 --> 함수 호출
# 함수 호출 시 정의된 함수의 argumentlist에 맞도록 데이터 전달

# 함수 정의
def print_3_times(*value, data='test') :
    for i in range(3) :
        print("{0} : hello function {1}".format(i,value))

# 함수 호출
print_3_times('test1', 'test2')
print_3_times()
print_3_times('test1', 'test2', 'test3', data='test5')

def argument_test(a, b=10, c=20) :
    print("{0} : {1} : {2}".format(a,b,c))

argument_test(10) # b,c 는 기본값 : 10:20:30
argument_test(b=200,c=300,a=100) # 순서상관없이 변수 값에 매핑 100:200:300
argument_test(1000, 2000, 3000) # 순서대로 매핑 1000:2000:3000

def return_none_test() :
    return                 # return : function 종료 - 호출한 곳으로

print(return_none_test())  # return data 없을 경우 None

def return_test(a,b) :
    sum = a+b
    return sum

print(return_test(10,20))

# 전달되는 가변 매개변수 곱해서 리턴하기
def multi(*values) :
    result = 1
    for value in values :
        result * value
    return result

print(multi(5,7,9,10))

# tuple : 값 변경하지 않는 list tuple 변수 = (value, value, ...)
tuple_data = (10,20,30,40,50) #cf
list_data = [10,20,30,40,50]

for tdata in tuple_data :
    print(tdata, end = " ")
print()
for ldata in list_data :
    print(ldata, end = " ")

list_data[0] = 100
# tuple_data[0] = 100 // TypeError : 값 변경 할 수 없음