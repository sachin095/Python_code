 #Iterate through every number in a list to separate out even 
 #and odd numbers. Identify possible outlier values as well.
my_list = [2,3,4,6,7,88,99,22,44,66,22,77,5,17,11,13]
even = []
not_even = []
for i in my_list:
    if i%2==0:
       even.append(i)
    else:
        not_even.append(i)
print("even number",even)
print("odd number",not_even)
