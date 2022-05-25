import pyautogui
import time

time.sleep(3)
print("Let's go...........")
#time.sleep(1)
message = """Damn you bro.

"""                          
for j in range(50):     
    for i in message:
        pyautogui.typewrite(i)
        
