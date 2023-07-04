

swim_min= int(input ('Enter swimming time results in minutes: '))
run_min= int(input('Enter running time results in minutes: '))
cycle_min=int(input('Enter Cycling time results in minutes: '))

#calculate the total time time to complete triathlon
total_min = int(swim_min+run_min+cycle_min)

#from the total allcate the right award 

#within qualifiying time
if total_min <=100:
    print('The award to be recieved = PROVINCIAL COLOURS ')

elif total_min <=105:
    print('The award to be recieved = HALF PROVINCIAL COLOURS')

elif total_min<=110:
    print('The award to be recieved = PROVINCIAL SCROLL')
else  :
    print ('Outside qulifiying time, no award recieved')

