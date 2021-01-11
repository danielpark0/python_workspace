hello="안녕하세요" #문자열 배열 : 0~len() -1
num_string=input("숫자 입력 : ")
print(hello[1:3]) #index 1부터 (3-1)개 문자열
print(len(hello)) #문자열 형식 지정 IndexError 주의
print("문자열 길이는 {0} 입니다.".format(len(hello),hello)) #문자열 형식 지정 IndexError 주의
print(hello.upper())
print(hello.lower())
print(hello.strip())
print("{0} 이 숫자인가?".format(num_string.isdecimal()))
if(num_string.isalnum()) : num = int(num_string)