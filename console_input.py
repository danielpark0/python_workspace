data = input("data : ")

original_data = 100
#sum = original_data+data # Type error
sum = original_data + int(data) # type cast : ValueError
print(sum)
sum = 10+10.5
print(type(sum))