import datetime

print("This is my first python on GitHub : \"Basic Alarm Clock\" ")

print("Please type your wake up time in 24 Hour format \"HH MM\". ")
hh = int(input("Wakeup Hour:  "))
mm = int(input ("Wakeup Minute:  "))
while(1==1):
	if hh in range(1, 25): #I written max range 25, as 24 range taking 23 as correct input and 24 hour is incorrect
		if int(mm) in range(-1, 61): #I written min range -1, as 0 range taking 1 as correct input and 00 minute is incorrect
			if (hh == datetime.datetime.now().hour and mm == datetime.datetime.now().minute):
				print("Wake Up Vikas, Its time to RUN")
				break
		else: 
			print("You have entered incorrect Minutes, Please try again later")
			break
	else: 
		print("You have entered incorrect Hours, Please try again later")
		break