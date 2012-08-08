import time
import win32api, win32con

VK_CODE = {'spacebar':0x20}

def press(x):
    win32api.keybd_event(VK_CODE[x], 0,0,0)
    win32api.keybd_event(VK_CODE[x],0 ,win32con.KEYEVENTF_KEYUP ,0)

def play():
	time.sleep(1)
	print "START!!"
	s = time.time()
	while time.time() - s < 25 :
		press('spacebar')  
		time.sleep(0.25)
		
		while (time.time() - s >= 6) and (time.time() - s < 13):
			press('spacebar')  
			time.sleep(0.5)
		
		while (time.time() - s >= 13) and (time.time() - s < 20):
			press('spacebar')  
			time.sleep(0.65)
			
		while (time.time() - s >= 20) and (time.time() - s < 25):
			press('spacebar')  
			time.sleep(0.8)
play()