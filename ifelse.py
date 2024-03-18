eng = int(input("enter your marks: "))
mat = int(input("enter your marks: "))
phy = int(input("enter your marks: "))
che = int(input("emter your marks: "))
bio = int(input("enter your marks: "))
total = eng + mat + phy + che + bio
per = total/5
if eng >= 32 and mat >= 32 and phy >= 32 and che >= 32 and bio >= 32: 
    if per > 80 or per == 80:
     print("a")
    
    elif per > 60 or per == 60:
     print("b")
    
    elif per > 40 or per == 40:
     print("d")
    else:
     print("fail")
    print("total =" ,total)
    print("percentage =" ,per)
    print("eng  mat  phy  che  bio:" ,eng, mat, phy, che, bio)
else:
    print("grade = F")
