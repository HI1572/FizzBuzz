'''
Lucio
Febuary 3, 2022
This code is used in job interviews to test you.
'''
for x in range(1, 101): #From 1 to 100
    if x % 15 == 0: #If multiple of 15 
        print('Fizz Buzz')
    
    elif x % 3 == 0:
        print('Fizz')
        
    elif x % 5 == 0:
        print('Buzz')
        
    else:
        print(x)