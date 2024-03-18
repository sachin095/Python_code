info = {'name': 'sachin' , 'cast' :'gautam','age':22, 'bool': 2}
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
    print(info.items())