i = 0
count=0

a = "sachin gautam"
print(a[0:4])
print(len(a))
print(a[::-1])
print('s' in a)
print('pari' not in a)
print(r'C://sachin') # prints C://python37 as it is written    

# del(a)
#we can use del function to delete string 

for i in range (len(a)):
    if a[i]==" ":
        print(i)
        
        count=i+1
        i = i+1
print(count)
