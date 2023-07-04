
#ask the user to enter a number
num= int(input('Enter a whole number or -1 to exit: '))
#we want to calculate the number the number of user entries
sum =0 #stores +ve numbers the user enters 
count=0 # How many numbers the user has entered

while num >= 0:
    sum+= num #
    count += 1
    num= int(input('Enter a whole number or -1 to exit '))
   
#when num =-1 loop stops and counts number of entiries 
if count >0: #incase 1st input is -1 we wont be able to calculate entries
        print('You have entered -1 to stop')
   #calculate average of the numbers entered sum/count
        print(f'The average of the number entered is {sum/count}')
    

elif count<=0:
    print('You have not entered a whole number before exiting')
    
    num= int(input('Enter a whole number or -1 to exit: '))
#we want to calculate the number the number of user entries
    sum =0 #stores +ve numbers the user enters 
    count=0 # How many numbers the user has entered
    while num >= 0:
        sum+= num #
        count += 1
        num= int(input('Enter a whole number and -1 to exit: '))

    
#when num =-1 loop stops and counts number of entiries 
    if count >0: #incase 1st input is -1 we wont be able to calculate entries
        print('You have entered -1 to stop')
   #calculate average of the numbers entered sum/count
        print(f'The average of the number entered is {sum/count}') 

else:
    print('You have not entered a number to calcute the average ') # if no number typed 
    
    num= int(input('Enter a whole number or -1 to exit: '))
#we want to calculate the number the number of user entries
    sum =0 #stores +ve numbers the user enters 
    count=0 # How many numbers the user has entered

    while num >= 0:
        sum+= num #
        count += 1
        num= int(input('Enter a whole number or -1 to exit '))
   
#when num =-1 loop stops and counts number of entiries 
    if count >0: #incase 1st input is -1 we wont be able to calculate entries
        print('You have entered -1 to stop')
   #calculate average of the numbers entered sum/count
        print(f'The average of the number entered is {sum/count}')
    

    elif count<=0:
        print('You have not entered a whole number before exiting')
    
        num= int(input('Enter a whole number or -1 to exit: '))
#we want to calculate the number the number of user entries
        sum =0 #stores +ve numbers the user enters 
        count=0 # How many numbers the user has entered
       
        while num >= 0:
            sum+= num #
            count += 1
            num= int(input('Enter a whole number and -1 to exit: '))

    
#when num =-1 loop stops and counts number of entiries 
        if count >0: #incase 1st input is -1 we wont be able to calculate entries
            print('You have entered -1 to stop')
   #calculate average of the numbers entered sum/count
            print(f'The average of the number entered is {sum/count}') 