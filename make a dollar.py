# make a dollar
# 5c, 10c, 25c

permutation = []

for i in range(0,101,25):
    for j in range (0,101,10):
        for k in range (0,101,5):
            if i+j+k == 100:
                print (i,j,k)

