name = input('Please enter your full name \n ')

if len(name)==0:
    print("You haven't entered anything. Please enter your full name.") 
elif len(name)<4:
        print("You have entered less than 4 characters. Please make sure that you have entered your name and Surname") 
elif len(name)>25:
        print("You have entered more than 25 characters. Please make sure that you have only entered your name.")
else:
    print("Thank you for entering your full name.")