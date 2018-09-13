from pygame import mixer 
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(11, GPIO.IN)
wait = 0.25
count = 0
mixer.init()

class pinCheck:
    isLoaded = False
    isPaused = False
    
    def __init__(self, song):
        self.song = song

    def hasStarted(self):
        if self.isLoaded == False:
            return 'NULL'
        if mixer.music.get_pos() < 10000:
            return False
        else:
            return True

    def isPlaying(self):
        if self.isLoaded == False:
            return False
        else:
            return mixer.music.get_busy()
 
    def loadSong(self):
        mixer.music.load(self.song)
        self.isLoaded = True

    def playSong(self): 
        if self.isLoaded == False:
            print('Error: no song loaded')
        else:
            mixer.music.play()
        
    def musicStop(self):
        mixer.music.stop()
        mixer.quit()
        mixer.init()
        self.isLoaded = False

    def pauseSong(self):
        if self.isPlaying():
            mixer.music.pause()
            self.isPaused = True
            return True
        else:
            return False

    def unPause(self):
        if self.isPaused == True:
            mixer.music.unpause()
            self.isPaused = False
            return True
        else:
            return False

class songPlayer(pinCheck):

    def pauseResume(self):
        if self.isPaused == True:
            self.unPause()
        else:
            self.pauseSong()

    def fullLoad(self):
        if self.isLoaded == False:
            self.loadSong()

    def playSongFT(self):
        if self.hasStarted() == False:
            self.playSong()
        
    def fullUnload(self):
        self.musicStop()

songOne = songPlayer('shootingmemes.mp3')
songTwo = songPlayer('allwinters.mp3')
initialize = songPlayer('wiisongyo.mp3')
songFour = songPlayer('theworst.mp3') 
songFive = songPlayer('nevergongive.mp3')
songSix = songPlayer('greenday.mp3')
songSeven = songPlayer('deathstar.mp3')
songThree = songPlayer('gtheme.mp3')

cur = initialize
cur.fullLoad()
cur.playSongFT()

while True:
    if GPIO.input(12) == True: #if the button is pressed
        if GPIO.input(11) == True and GPIO.input(13) == True and GPIO.input(15) == True: #combination one of 111
            print('Button combo 111 Active!')
            if cur == songOne: #check to see if the switches are still the same
                #print('songOne pause')
                
                cur.pauseResume()
                sleep(wait)
            else:
                cur.fullUnload() #cease playing the previous song, set the new one to the current, load and play it
                #print('songOne Unload')
                #sleep(1)

                cur = songOne
                #print('cur set')
                #sleep(1)

                cur.fullLoad()
                #print('full Load Done!')
                #sleep(1)
                
                cur.playSong()
                #print('song playing!')
                #sleep(1)
                sleep(wait)
				
        if GPIO.input(11) == True and GPIO.input(13) == True and GPIO.input(15) == False: #combination of 110
            if cur == songTwo:
                cur.pauseResume()
                sleep(wait)
            else:
                cur.fullUnload()
                cur = songTwo
                cur.fullLoad()
                cur.playSong()
                sleep(wait)
				
        if GPIO.input(11) == True and GPIO.input(13) == False and GPIO.input(15) == True: #combination of 101
            if cur == songThree:
                cur.pauseResume()
                sleep(wait)
            else:
                cur.fullUnload()
                cur = songThree
                cur.fullLoad()
                cur.playSong()
                sleep(wait)
		
        if GPIO.input(11) == True and GPIO.input(13) == False and GPIO.input(15) == False: #combination of 100
            print('selected song4')
            if cur == songFour:
                print('pause song4')
                cur.pauseResume()
                sleep(wait)
            else:
                cur.musicStop()
                print('stop song4')
                cur = songFour
                print('cur set song4')
                cur.fullLoad()
                print('load song4')
                cur.playSong()
                print('play song4')
                sleep(wait)
		
        if GPIO.input(11) == False and GPIO.input(13) == False and GPIO.input(15) == True: #combination of 001
            if cur == songFive:
                cur.pauseResume()
                sleep(wait)	
            else:
                cur.musicStop()
                cur = songFive
                cur.fullLoad()
                cur.playSong()
                sleep(wait)
				
        if GPIO.input(11) == False and GPIO.input(13) == True and GPIO.input(15) == False: #combination of 010
            if cur == songSix:
                cur.pauseResume()
                sleep(wait)			
            else:
                cur.musicStop()
                cur = songSix
                cur.fullLoad()
                cur.playSong()
                sleep(wait)
		
		
        if GPIO.input(11) == False and GPIO.input(13) == True and GPIO.input(15) == True: #combination of 011
            if cur == songSeven:
                cur.pauseResume()
                sleep(wait)
					
            else:
                cur.musicStop()
                cur = songSeven
                cur.loadSong()
                cur.playSong()
                sleep(wait)
    else:
         #print(count)
        sleep(0.001)
        count = count + 1
    if count == 500000:
        break
	
GPIO.cleanup()
mixer.quit()
print('done!')


