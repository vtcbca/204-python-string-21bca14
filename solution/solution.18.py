#WAS to Enter 5 string in a list and check and print string whose lent has even number of character without any string function.
l=[]
def creatlist():
    for i in range(2):
        s=input("Enter string:")
        l.append(s)
    return(creatlist)

def evennumber (l):
    count=0
    for i in l:
        for j in i:
            if(j%2==0):
                print("Total string of even {} character:".format(j))
                count+=1
    return(evennumber)
a=creatlist()
ans=evennumber(l)
print(ans)                     


