# 1. print all numbers divisible by 5 and then by 8 from 2000 to 2500
for i in range(2000,2501):
    if i%5==0 and i%8==0:
        print(i)

# 2. print multiplication table of number using for loop
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)