#Advanced task one
'''
def addtoarray(num):
    userarray=[]
    for i in range(1,int(num)+1):
        userarray.append(i)
    return userarray
userstring=""
print("Enter a number (preferrably between 1 and 9)")
usernum=int(input())
for i in addtoarray(usernum):
    for n in range(0, i):
        userstring=userstring+str(i)
    print(userstring)
    userstring=""
'''

#Advanced task two

pointer=0
print("Enter a number (preferrably large)")
usernum=int(input())

if type(usernum[pointer])!=int:
    print(usernum[pointer+1])
else:
    print(usernum[pointer])