# info = {1:{"name":"sachin","age":18,"add":"kathmandu"},
#         2:{"name":"gautam","age":33,"add":"kapilbastu"},
#         3:{"name":"sandip","age":19,"add":"morang"}}
# # print(info)
# print(info[1])
info = []
n = int(input("enter any value"))
for i in range(n,n+1):
    name=input("enter name =")
    age=input("enter age=")
    add = input("enter address=")
    # l=int(input("enter number ="))
    info = {'name':name,'ntc':age,'ncell':add}
    info[i] = info
    # l.append(d)
print(info)
info[3]['add']={'per':"jhapa",'temp':'dhulikhel'}
print(info)