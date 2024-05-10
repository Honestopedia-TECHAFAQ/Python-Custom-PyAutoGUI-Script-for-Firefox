import pyautogui
import time
import tkinter as tk

def switch_to_firefox():
    print("Switching to Firefox...")

def press_yes_or_no(yes=True):
    if yes:
        print("Pressing Yes")
    else:
        print("Pressing No")

def navigate_and_select(button_count, last_button=None):
    for _ in range(button_count):
        pyautogui.press('tab')
        time.sleep(0.5)
    if last_button is not None:
        print("Navigated to the last button")

def hotkey_handler(event):
    if event.keysym == '7' and event.state == 4: 
        switch_to_firefox()
        navigate_and_select(3)
        press_yes_or_no()
    elif event.keysym == '9' and event.state == 4:  
        switch_to_firefox()
        navigate_and_select(5, last_button=True)
        press_yes_or_no(yes=False)

def ctrl_7_pressed():
    event = tk.Event()
    event.keysym = '7'
    event.state = 4
    hotkey_handler(event)

def ctrl_9_pressed():
    event = tk.Event()
    event.keysym = '9'
    event.state = 4
    hotkey_handler(event)
root = tk.Tk()
root.title("Hotkey GUI")
label_1 = tk.Label(root, text="Press Ctrl+7 to perform action 1")
label_1.pack()

label_2 = tk.Label(root, text="Press Ctrl+9 to perform action 2")
label_2.pack()
root.bind("<Control-Key-7>", lambda event: ctrl_7_pressed())
root.bind("<Control-Key-9>", lambda event: ctrl_9_pressed())

root.mainloop()
