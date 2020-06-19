mylist = [1, 1, 2,2, 4,4,50, 50,93, 93, 95, 99, 99, 100,100]

while len(mylist) > 1:
    mylist_len = len(mylist)
    middle = int(mylist_len/2)

    if mylist[middle] != mylist[middle-1] and mylist[middle] != mylist[middle+1]:
        print (mylist[middle])
        break

    if middle%2 == 0:
        if mylist[middle] == mylist[middle+1]:
            mylist = mylist[middle:mylist_len+1]
            
        else:
            mylist = mylist[:middle]

    elif middle%2 != 0:
        if mylist[middle] == mylist[middle+1]:
            mylist = mylist[:middle]
           
        else:
            mylist = mylist[middle+1:mylist_len+1]
print (mylist)


'''
for i in range (0,mylist_len-1):
    if mylist [i] == mylist[i+1]:
        i = i + 2
    else:
        unique.append(mylist[i])
 '''    
'''
unique = []
i = 0
mylist_len = len(mylist)
while i < mylist_len-1:

    if mylist [i] == mylist[i+1]:
        i = i + 2
    else:
        unique.append(mylist[i])
        i = i+1

print (unique)

'''