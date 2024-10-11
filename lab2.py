def addtoarray(num):
    userarray=[]
    for i in range(1,int(num)+1):
        userarray.append(i)
    return userarray

userstring=""
print("Enter a number")
usernum=int(input())
for i in addtoarray(usernum):
    for n in range(0, i):
        userstring=userstring+str(i)
    print(userstring)
    userstring=""