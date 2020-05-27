import datetime
import simpleaudio as player
#print("This is my first python on GitHub : \"Basic Alarm Clock\" ")
s1 = 'Sound_1.wav'
s2 = 'Sound_2.wav'
s3 = 'Sound_3.wav'
print("Please type your wake up time in 24 Hour format \"HH MM\". ")
hh = int(input("Wakeup Hour:  "))
mm = int(input ("Wakeup Minute:  "))
selection = int(input("Which sound you want to play, Enter 1, 2 or 3:"))

while(1==1):
	if hh in range(1, 25): #I written max range 25, as 24 range taking 23 as correct input and 24 hour is incorrect
		if int(mm) in range(-1, 61): #I written min range -1, as 0 range taking 1 as correct input and 00 minute is incorrect
			if (hh == datetime.datetime.now().hour and mm == datetime.datetime.now().minute):
				print("Wake Up Vikas, Its time to RUN")
				if(selection==1):
					song = player.WaveObject.from_wave_file(s1)
					play_song = song.play()
					play_song.wait_done()  # Wait until song has finished playing.
				elif(selection==2):
					song = player.WaveObject.from_wave_file(s2)
					play_song = song.play()
					play_song.wait_done()  # Wait until song has finished playing.
				elif(selection==3):
					song = player.WaveObject.from_wave_file(s3)
					play_song = song.play()
					play_song.wait_done()  # Wait until song has finished playing.
				else:
					print("unfortunately you have not selected the songs from given numbers")
				break
		else: 
			print("You have entered incorrect Minutes, Please try again later")
			break
	else: 
		print("You have entered incorrect Hours, Please try again later")
		break