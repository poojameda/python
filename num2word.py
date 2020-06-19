#num2roman = {1:"I", 5: 'V', 10: "X", 50:"L"}
special4 = {0:"IV",1:"XL", 2: "CD"}
special9 = {0:"IX",1:"XC", 2: "CM"}

romanLower3 = {0:"I", 1:"X", 2:"C", 3:'M'}
romanUpper3 = {0:"V", 1:"L", 2:"D"}

num2convert = input("Type a number less than 1000: ")
length = len(num2convert)
output = []

def get(place, inp):
    if inp == 4:
        output.append(special4[place])
    elif inp == 9:
        output.append(special9[place])
    elif inp >=1 and inp <=3:
        output.append(romanLower3[place]*inp)
    elif inp >=5 and inp <=8:
        output.append(romanUpper3[place])
        remaining = inp - 5
        output.append(romanLower3[place]*remaining)
        


for num in range(0,length):
    place = length-num-1
    chr = num2convert[num]
    get(place,int(chr))
    
print("".join(output))

# ones = int(num2convert%10)

# tens = int(int(num2convert - ones)/10)



# for i in range(1,tens+1):
#     output.append(num2roman[10])

# if ones == 4:
#     output.append("IV")
# elif ones == 9:
#     output.append("IX")
# elif ones >= 1 and <= 3:
#     output.append(ones*num2roman[1])
# elif ones >= 5 and ones <==8:
#     output.append(num2roman[5])
#     output.append(ones*num2roman[1])

# print (output)


# print(tens)
# print(ones)


