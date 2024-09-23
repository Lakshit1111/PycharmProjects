import pyautogui as muz
import time

message = ["Pagal","Piss off" ,"Monkey" , "Moti" ,"Hipo" , "POOOOOP" , "Piggi"]
time.sleep(5)

for i in range(10):
    for j in message:
        muz.typewrite(j.upper())
        muz.press("Enter")