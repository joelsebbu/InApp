# regular expression
import re

# Question 1:
ipAddr = '239.08.006.139'
ip = re.sub('0','',ipAddr) # remove 0 from ip address
print(ip)

# Question 2:

a='An apple a day keeps the doctor away'
aa=re.findall(r'ap\w+',a)
print(aa)

# Question 3:

a= re.sub('apple','orange',a)
a= re.sub('doctor','cat',a)
print(a)