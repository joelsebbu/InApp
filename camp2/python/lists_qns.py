# 1. sort list and print first element
list=[6,2,3,0,1,7,8,9,4,5]
list.sort()
print(list[0])

# 2. print second element
print(list[1])

 # 3. list of numbers append even numbers and odd numbers
 # to respective lists
even_list=[]
odd_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)

# 4. reverse list
list.reverse()
print(list)

# 5. print odd numbers from 1 to 50
for i in range(1,50):
    if i%2 != 0:
        print(i)

# 6. print count of even and odd numbers in list usinf for loop
even_count=0
odd_count=0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)