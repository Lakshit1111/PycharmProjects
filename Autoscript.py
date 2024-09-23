import pyautogui
import tkinter
import time

time.sleep(5)
clipboard_content = tkinter.Tk().clipboard_get()
# print(clipboard_content.split("\n"))
# cc =clipboard_content.split("\n")
d = [i.strip() for i in clipboard_content.split("\n")]
print(d)

for i in d:
    pyautogui.write(i, interval=0)
    pyautogui.press("return")


