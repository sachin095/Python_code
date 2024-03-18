l = []
n = int(input("enter any value"))
for i in range(n):
    name=input("enter name =")
    ntc = int(input("enter number="))
    ncell = int(input("enter number="))
    # l=int(input("enter number ="))
    d = {'name':name,'ntc':ntc,'ncell':ncell}
    l.append(d)
print(l)