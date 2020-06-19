user_input = input("Enter a number: ") 

length = len(str(user_input))
'''
# Brute force
i = 0

while i < int(length/2):
    if user_input[i] == user_input[length-1-i]:
        i = i + 1
    else:
        user_input = str(int(user_input)+1)
        i=0
        
print (user_input)
'''
i=0
user_input = list(user_input)

while i < int(length/2):
    if user_input[i] != user_input[length-1-i] and int(user_input[i]) < int(user_input[length-1-i]):
        user_input[length-1-i] = user_input[i]
        user_input[length-1-i-1] = int(user_input[length-1-i-1]) + 1

    elif user_input[i] != user_input[length-1-i] and int(user_input[i]) > int(user_input[length-1-i]):
        user_input[length-1-i] = user_input[i]
    
    elif user_input[i] == user_input[length-1-i]:
        i=i+1

print(user_input)